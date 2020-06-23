from enum import Enum
from BinaryTree import BinaryTree
from collections import deque
class Order(Enum):
    IN = 0
    PRE = 1
    POST = 2
    LEVEL = 3

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def add_node(self, data):
        # check if no self.root then set this as root else traverse to find the correct position of node in BST

        if not self.root:
            self.root = TreeNode(data)
            return

        else:
            root = self.root

            def helper(node, data):

                if data <= node.val:
                    if node.left:
                        helper(node.left, data)
                    else:
                        node.left = TreeNode(data)

                else:
                    if node.right:
                        helper(node.right, data)
                    else:
                        node.right = TreeNode(data)

            helper(root, data)

    def _inorder(self, node, path):

        if not node:
            return
        if node:
            self._inorder(node.left, path)
            path.append(node.val)
            self._inorder(node.right, path)

    def _preorder(self, node, path):

        if not node:
            return
        if node:
            path.append(node.val)
            self._preorder(node.left, path)
            self._preorder(node.right, path)

    def _postorder(self, node, path):

        if not node:
            return
        if node:
            path.append(node.val)
            self._preorder(node.left, path)
            self._preorder(node.right, path)


    def _level_order(self, node, path):

        prev_level = 1
        q = deque([(node, 1)])
        temp = []
        while q:

            next_node, level = q.popleft()

            if prev_level < level:
                path.append(temp)
                prev_level = level
                temp = []

            temp.append((next_node.val))
            if next_node.left:
                q.append((next_node.left, level+1))
            if next_node.right:
                q.append((next_node.right, level+1))
        if len(temp) != 0:
            path.append(temp)


    def traverse(self, order):
        root = self.root
        path = []
        if order == Order.IN.value:
            self._inorder(root, path)

        elif order == Order.PRE.value:
            self._preorder(root, path)

        elif order == Order.POST.value:
            self._postorder(root, path)

        elif order == Order.LEVEL.value:
            self._level_order(root, path)

        for node in path:
            print node,


def is_valid(root, lower, upper):

    if not root:
        return True

    if root.val <= lower or root.val > upper:
        return False

    return is_valid(root.left, lower, root.val) and is_valid(root.right, root.val, upper)


# btree = BinaryTree()
# root = btree.create_tree_from_array([3,6,2,4,6,7,1,9])
# btree.inorder(root)
# print is_valid(root, float('-inf'), float('inf'))
# root = btree.create_tree_from_array([5, 3, 8, 1, 4, 6, 9])
# print is_valid(root, float('-inf'), float('inf'))
bst = BinarySearchTree()
bst.add_node(5)
bst.add_node(3)
bst.add_node(8)
bst.add_node(1)
bst.add_node(4)
bst.add_node(6)
bst.add_node(9)
bst.traverse(3)
# bst.traverse(0)
# print
# bst.traverse(1)
# print
# bst.traverse(2)











