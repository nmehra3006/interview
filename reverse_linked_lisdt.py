class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):

    prev = None
    curr = head
    while curr:

        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def reverse_linked_list_recursive(currNode, nextNode):

    if currNode == None or nextNode == None:
        return currNode


    nextNext = nextNode.next
    nextNode.next = currNode
    return reverse_linked_list_recursive(nextNode, nextNext)



def print_list(head):
    print "\n"
    curr = head
    while curr:
        print curr.val,
        curr = curr.next

# [1,2,3] - > [3,2,1]
# [] - > []
# [1] - > [1]

head = Node(1)
head.next = Node(2)
#head.next.next = Node(3)
print_list(head)


new_head = reverse_linked_list_recursive(head, head.next)
head.next = None
print_list(new_head)
# new_head = reverse_linked_list(head)
# print_list(new_head)


