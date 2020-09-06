'''
Reversing a singly LInked List
'''
def reverse_list(head):
    current = head
    previuos = None
    nextnode = None
    while current != None:
        nextnode = current.nextnode
        current.nextnode = previuos
        previuos = current
        current = nextnode
    return previuos

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def print_list(head):
    while head:
        print (head.value,end = " ")
        head = head.nextnode
    print()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d
print_list(a)
new_head = reverse_list(a)
print_list(new_head)