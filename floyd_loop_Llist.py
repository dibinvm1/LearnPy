'''
Finding out if there is a loop in the given linked list
'''

def loop_finder(node):
    fast_N = node
    slow_N = node
    while fast_N != None and fast_N.nextnode != None:
        slow_N = slow_N.nextnode
        fast_N = fast_N.nextnode.nextnode
        if fast_N == slow_N:
            return True
    return False

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # loop

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y 
y.nextnode = z # no loop

print (loop_finder(a))
print(loop_finder(x))