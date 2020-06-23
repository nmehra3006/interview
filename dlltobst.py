global head

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def dlltobst(size=2):
    global head
    if size <= 0:
        return None

    left = dlltobst(size / 2)
    root = Node(head.val)

    root.left = left

    head = head.next

    root.right = dlltobst(size - int(size/2) - 1)

    return root


l = Node(4)
l.next = Node(5)
l.next.prev = l
head = l
dlltobst(2)







