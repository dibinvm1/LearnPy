'''
Creating queue using 2 stacks
'''
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
q =Queue()
q.enqueue(1)
q.enqueue(8)
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
for i in range(5):
    print(q.dequeue())
