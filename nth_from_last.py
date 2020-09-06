'''
given head node and a N Returns Node from N'th from last
'''
def seach_node(n,head):
    right = head
    left = head
    for i in range(n-1): #Goes till max N to create a block
        if not right.nextnode:
            print("Error N is larger than Linked list Size")
            return
            #raise LookupError('Error N is larger than Linked list Size')
        right = right.nextnode
    while right.nextnode: #iterate till end and left pointer is the n'th node from last(other end of block)
        right = right.nextnode
        left = left.nextnode
    return left
class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d

node = seach_node(2,a)
print(node.value)