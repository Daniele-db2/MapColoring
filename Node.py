import random

class Node:
    def __init__(self):
        self.color = 0
        self.parent = None
        self.sons = []
        self.domain = []

    def setColor(self, D):
        if len(D) <= 1:
            return "Unsat", False
        else:
            ind = random.randrange(1,len(D))
            self.color = D[ind]

    def getColor(self):
        return self.color

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def addSon(self, son):
        self.sons.append(son)

    def setSon(self):
        self.sons = []

    def getSons(self):
        return self.sons

    def setDomain(self, D):
        lenght = random.randrange(3,len(D))
        for i in range (1,lenght):
            j = random.randrange(1,len(D))
            clr = D[j]
            self.domain.append(clr)
            self.domain = self.rmv()

    def getDomain(self):
        return self.domain

    def rmv (self):
        final_list = []
        for num in self.domain:
            if num not in final_list:
                final_list.append(num)
        return final_list