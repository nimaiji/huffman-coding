class node:

    def __init__(self,name = "node",value = 0):
        self.name = name
        self.value = value
        self.childs = []
        self.parents = []

    def addChild(self,child):
        self.childs += child

    def addParent(self,parent):
        self.parents += parent

    def removeChild(self,value):
        for child in self.childs:
            if (child.value == value):
                self.childs.remove(child)

    def removeParent(self,value):
        for parent in self.parents:
            if(parent.value == value):
                self.parents.remove(parent)