class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_node(self, val):
        node = Node(val)
        if self.count == 0:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.count += 1

    def print_list(self):

        curr = self.head

        while curr:
            print curr.val,
            curr = curr.next

    def delete_node(self, data):
        prev = Node(-1)
        prev.next = self.head
        curr = self.head

        while curr:
            if curr.val == data:
                prev.next = curr.next
                self.count -= 1
                curr = prev.next

            else:
                curr = curr.next
                prev = prev.next

        self.tail = prev

ll = LinkedList()
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.add_node(6)
ll.add_node(6)
ll.delete_node(6)
ll.print_list()
