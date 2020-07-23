'''
Simple Queue Implementation using deque
'''

from collections import deque
class Queue(object):
    def __init__(self):
        self.len = 0
        self.items = deque()
    def __len__(self):
        return self.len
    def isEmpty(self):
        return self.len == 0
    def enqueue(self,item):
        self.len += 1
        self.items.appendleft(item)
    def dequeue(self):
        if self.isEmpty():
            print("Can't dequeue Queue Empty!!")
            return
        self.len -=1
        return self.items.pop()
    def __str__(self):
        return str(self.items)

q = Queue()

print(q.isEmpty())
print(q.dequeue())
q.enqueue(1)
q.enqueue(8)
q.enqueue(2)
print(q.isEmpty())
print(q.dequeue())
print(q)