'''
Simple Collcection.deque Implementation
'''

class Deque(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addBack(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeBack(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
d = Deque()
print(d.isEmpty())
d.addBack(10)
d.addFront(9)
d.addFront(4)
d.addBack(1)
d.addBack(0)
d.addFront(5)
print(d.removeBack())
print(d.removeFront())
print(d.size())