'''
Simple Stack Implementation
'''

class Stack(object):
    def __init__(self):
        self.len = 0 #kept our own len var instead of len(self.items)
        self.items = []
    def __len__(self): #used len instead of size()
        return len(self.items)
    def isEmpty(self):
        return self.len == 0
    def push(self,item):
        self.len +=1
        self.items.append(item)
    def peek(self):
        if self.isEmpty():
            #raise IndexError("Empty Stack can't peek!!")
            print("Empty Stack can't peek!!") #to allow conitune running
            return
        return self.items[self.len-1]
    def pop(self):
        if self.isEmpty():
            #raise IndexError("Empty Stack can't pop!!")
            print("Empty Stack can't pop!!") ##to allow conitune running
            return
        self.len -=1
        return self.items.pop()
    def __str__(self):
        return str(self.items)

s =Stack()
print(s.isEmpty())
print(s.peek() , s.pop())
s.push(1)
s.push(3)
s.push(6)
s.push(2)
print(s)
print(s.peek() , s.pop())
print(len(s))
