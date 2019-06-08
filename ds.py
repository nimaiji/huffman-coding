import enum
import queue
import os


class dir(enum.Enum):
    LEFT = 0
    RIGHT = 1


class node:

    def __init__(self, name="node", value=0):
        self.name = name
        self.value = value
        self.childs = []
        self.parents = []
        self.dir = None
        self.headState = False

    def addChild(self, child):
        self.childs.append(child)

    def addParent(self, parent):
        self.parents.append(parent)
        parent.childs

    def removeChild(self, value):
        for child in self.childs:
            if child.value == value:
                self.childs.remove(child)

    def removeParent(self, value):
        for parent in self.parents:
            if parent.value == value:
                self.parents.remove(parent)

    def isHead(self):
        return self.headState

    def setHead(self):
        self.headState = True

    def unsetHead(self):
        self.headState = False

    def __str__(self):
        return self.name + " : " + str(self.value)


class tree:

    def __init__(self, head, name='tree', isPrefect=False):
        self.name = name
        self.isPrefect = isPrefect
        self.nodes = []

        if head.isHead:
            self.head = head
            head.setHead()
            self.nodes.append(head)
        else:
            raise Exception("Illegal node")

    def insertNode(self):
        pass

    def getSize(self):
        return len(self.nodes)


class minHeap(tree):

    def __init__(self, head, name='min heap', isPrefect=True):
        super().__init__(head, name, isPrefect)

    def popNode(self):
        return self.nodes.pop()

    def insertNode(self, newNode):
        # new node index
        cuIndex = len(self.nodes)

        # defining direction
        if cuIndex % 2 == 0:
            newNode.dir = dir.RIGHT
        else:
            newNode.dir = dir.LEFT

        self.nodes.append(newNode)
        self.heapify(cuIndex)

    def heapify(self, index):
        cuNode = self.nodes[index]
        if cuNode.dir == dir.LEFT:
            paNode = self.nodes[int((index - 1) / 2)]
        else:
            paNode = self.nodes[int((index - 2) / 2)]

        if cuNode.value < paNode.value:

            # Swap Nodes
            cuNode.value, paNode.value = paNode.value, cuNode.value
            cuNode.name, paNode.name = paNode.name, cuNode.name

            # If current node is head do not continue heapify
            if not paNode.isHead():
                if cuNode.dir == dir.LEFT:
                    self.heapify(int((index - 1) / 2))
                else:
                    self.heapify(int((index - 2) / 2))


class huffmanTree(tree):

    def __init__(self, head, name='huffman tree', isPrefect=True):
        super().__init__(head, name, isPrefect)
        self.q = queue.Queue()

    def insertNode(self, node1, node2):
        newNode = node("{},{}".format(node1.name, node2.name), node1.value + node2.value)
        newNode.addChild(node1)
        newNode.addChild(node2)
        if self.q.qsize() == 1:
            self.insertNode(self.q.get(), newNode)
        else:
            self.q.put(newNode)

    def insertSingleNode(self, child):
        headNode = self.q.get()
        newNode = node("{},{}".format(headNode.name, child.name), headNode.value + child.value)
        newNode.addChild(headNode)
        newNode.addChild(child)

    def generate(self, minHeap):
        for x in range(int(minHeap.getSize() / 2)):
            try:
                a = minHeap.popNode()
                b = minHeap.popNode()
                self.insertNode(a, b)
            except:
                self.insertSingleNode(a)

        self.head = self.q.get()
        return self

    # def __str__(self):
    #     return self.generateArray()


class huffman:

    def __init__(self, path):
        self.minHeap = None
        self.huffmanTree = None
        self.frequency = {'EOF': 0}
        self.path = path
        self.tablePath = ''
        self.tableDict = {}

    def generateFrequency(self):
        file = open(self.path, 'r')
        for line in file:
            for index, char in enumerate(line):
                # print(index,char)
                if char in self.frequency:
                    self.frequency.update({char: self.frequency[char] + 1})
                else:
                    self.frequency[char] = 1

    def generateMinHeap(self):
        item = self.frequency.popitem()
        head = node(item[0], item[1])
        self.minHeap = minHeap(head)
        for n in self.frequency:
            self.minHeap.insertNode(node(n, self.frequency[n]))

    def generateTree(self):
        self.generateFrequency()
        self.generateMinHeap()
        self.huffmanTree = huffmanTree(node('head', -1)).generate(self.minHeap)

    def generateTable(self, tablePath):
        self.tablePath = tablePath
        os.remove(tablePath)
        self.generateTable_helper('', 0, self.huffmanTree.head)

    def generateTable_helper(self, code, count, node):
        # print(code)
        if (node.childs == []):
            file = open(self.tablePath, 'a+')
            if node.name == '\n':
                file.write("{}\t{}\t{}\n".format('\\n', count - 1, code[1:]))
            elif node.name == '\t':
                file.write("{}\t{}\t{}\n".format('\\t', count - 1, code[1:]))
            else:
                file.write("{}\t{}\t{}\n".format(node.name, count - 1, code[1:]))
        else:
            for index, n in enumerate(node.childs):
                code += str(index)
                count += 1
                self.generateTable_helper(code, count, n)

    def tableToDict(self, tablePath):
        file = open(tablePath, 'r')
        for line in file:
            array = line.split('\t')
            array[2] = array[2].replace('\n', '')
            if array[0] == '\\n':
                self.tableDict['\n'] = array[2]
            elif array[0] == '\\t':
                self.tableDict['\t'] = array[2]
            else:
                self.tableDict[array[0]] = array[2]
            # print(array)
        # print(self.tableDict)
