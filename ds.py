import enum


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

    def removeChild(self, value):
        for child in self.childs:
            if (child.value == value):
                self.childs.remove(child)

    def removeParent(self, value):
        for parent in self.parents:
            if (parent.value == value):
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
        self.size = len(self.nodes)
        if (head.isHead):
            self.head = head
            head.setHead()
            self.nodes.append(head)
        else:
            raise Exception("Illegal node")

    def insertNode(self):
        pass


class minHeap(tree):

    def __init__(self, head, name='min heap', isPrefect=True):
        super().__init__(head, name, isPrefect)

    def insertNode(self, newNode):
        # new node index
        cuIndex = len(self.nodes)
        # defining direction
        if (cuIndex % 2 == 0):
            newNode.dir = dir.RIGHT
        else:
            newNode.dir = dir.LEFT

        self.nodes.append(newNode)
        self.heapify(cuIndex)

    def heapify(self, index):
        cuNode = self.nodes[index]
        if (cuNode.dir == dir.LEFT):
            paNode = self.nodes[int((index - 1) / 2)]
        else:
            paNode = self.nodes[int((index - 2) / 2)]

        if (cuNode.value < paNode.value):

            # Swap Nodes
            cuNode.value, paNode.value = paNode.value, cuNode.value
            cuNode.name, paNode.name = paNode.name, cuNode.name

            # If current node is head do not continue heapify
            if (not paNode.isHead()):
                if (cuNode.dir == dir.LEFT):
                    self.heapify(int((index - 1) / 2))
                else:
                    self.heapify(int((index - 2) / 2))
