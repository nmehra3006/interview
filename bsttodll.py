class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bsttodllutil(root):

    if root is None:
        return root

    if root.left:
        left = bsttodllutil(root.left)
        while left.right:
            left = left.right

        left.right = root
        root.left = left

    if root.right:

        right = bsttodllutil(root.right)
        while right.left:
            right = right.left

        right.left = root
        root.right = right


    return root


def bsttodll(node):

    if not root:
        return None

    node = bsttodllutil(root)

    while node.left:
        node = node.left

    return node


def print_list(head):
    """Function to print the given
       doubly linked list"""
    if head is None:
        return
    while head:
        print head.val,
        head = head.right


root = Node(10)

root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
head = bsttodll(root)
print_list(head)

