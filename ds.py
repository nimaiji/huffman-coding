class node:

    def __init__(self, name="node", value=0):
        self.name = name
        self.value = value
        self.childs = []
        self.parents = []

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
        return self.parents == []


class tree:

    def __init__(self, head, name='tree', isPrefect=False):
        self.name = name
        self.isPrefect = isPrefect
        if (head.isHead):
            self.head = head
        else:
            raise Exception("Illegal node")

    def insertNode(self):
        pass


class minHeap(tree):

    def __init__(self, head, name='min heap', isPrefect=False):
        super().__init__(head, name, isPrefect)
