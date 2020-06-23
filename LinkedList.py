import random
import heapq as hq
class ListError(Exception):

    def __init__(self, message):
        self.message = message

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

    def add_loop(self):
        idx = random.randint(1, self.count)
        curr = self.head
        i = idx
        while i > 0:
            curr = curr.next
            i -= 1
        self.tail.next = curr

        return idx, curr.val

    def add_all_nodes(self, arr):

        for i in range(len(arr)):
            self.add_node(arr[i])

        return self.head

    def print_list(self):
        print "\n"
        curr = self.head

        while curr:
            print curr.val,
            curr = curr.next

    def delete_node(self, data):
        if self.count == 0:
            raise ListError("No nodes in list")

        # delete first node
        while self.head.val == data and self.head:
            self.head = self.head.next
            self.count -= 1

        # delete in middle
        prev = self.head
        curr = prev.next

        while curr != self.tail:
            if curr.val == data:
                prev.next = curr.next
                self.count -= 1
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next

        # delete the tail
        if curr.val == data:
            prev.next = None
            self.count -= 1
            self.tail = prev

    def reverse(self):

        prev = None
        curr = self.head
        self.tail = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # what happens to self.tail
        self.head = prev

    def _start_cycle(self, fast):
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def detect_loop(self):

        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                start = self._start_cycle(fast)
                return True, start.val

        return False, -1



def merge_two_lists(list1, list2):
    merged_list = LinkedList()
    node1 = list1.head
    node2 = list2.head

    while node1 and node2:
        if node1.val <= node2.val:
            merged_list.add_node(node1.val)
            node1 = node1.next
        else:
            merged_list.add_node(node2.val)
            node2 = node2.next

    while node1:
        merged_list.add_node(node1.val)
        node1 = node1.next

    while node2:
        merged_list.add_node(node2.val)
        node2 = node2.next

    return merged_list


def merge_n_lists(list_of_lists):

    # [1,2,3,4] , [1,1,1], [4,5] = > [1,1,1,1,2,3,4,4,5]
    # solution with heap sort
    merged_n_list = LinkedList()

    heap = []

    for list in list_of_lists:
        curr = list
        hq.heappush(heap, (curr.head.val, curr.head))

    while heap:

        next_node = hq.heappop(heap)
        merged_n_list.add_node(next_node[0])
        if next_node[1].next is not None:
            hq.heappush(heap, (next_node[1].next.val, next_node[1].next))

    return merged_n_list


def print_list(head):
    curr = head
    while curr:
        print curr.val,
        curr = curr.next


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
head1 = ll1.add_all_nodes([1,1,1,1,1])
head2 = ll2.add_all_nodes([1,2,3,4,5,6])
ll3.add_all_nodes([8, 9, 10])
merged_list = merge_two_lists(ll1, ll2)
merged_list.print_list()
merged_n_list = merge_n_lists([ll1, ll2, ll3])
merged_n_list.print_list()
# ll.print_list()
# ll.delete_node(1)
# ll.print_list()
# ll.reverse()
# ll.print_list()
# print "\nloops"
# print ll.detect_loop()
# print ll.add_loop()
# print ll.detect_loop()
ll = LinkedList()
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.add_node(6)
ll.add_node(6)
ll.delete_node(6)
ll.print_list()
