from collections import deque
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinaryTree(object):

    def __init__(self):
        self.root = None

    # def add_node(self, data):
    #     new_node = TreeNode(data)
    #
    #     if not self.root:
    #         self.root = new_node
    #
    #     else:
    #         if self.root.left is None:
    #             self.root.left = new_node
    #         else:
    #             self.add_node

    def create_tree_from_array(self, arr):

        if len(arr) == 0:
            return None

        elif len(arr) == 1:
            self.root = TreeNode(arr[0])
            return self.root

        def helper(arr, i):
            if i >= len(arr):
                return None

            if i < len(arr):
                root = TreeNode(arr[i])
                root.left = helper(arr, 2*i+1)
                root.right = helper(arr, 2 * i + 2)

            return root
        self.root = helper(arr, 0)
        return self.root

    def get_path(self, root, node, path):

        if root.val == node:
            return True

        path.append(root.val)

        if root.left and self.get_path(root.left, node, path) or root.right and self.get_path(root.right, node, path):
            return True

        path.pop()
        return False

    def lca(self, root, node1, node2):

        path1 = []
        path2 = []

        if not self.get_path(root, node1, path1) or not self.get_path(root, node2, path2):
            return None

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i-1]

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print root.val
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print root.val
            self.inorder(root.left)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)

            print root.val

    def level_order_traversal(self, root):

        queue = deque([])
        prev_level = 1
        queue.append((root, 1))
        res = []
        level_wise_list = []
        while queue:
            node, level = queue.popleft()

            if prev_level < level:
                prev_level = level
                res.append(level_wise_list)
                level_wise_list = []

            level_wise_list.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        if len(level_wise_list) != 0:
            res.append(level_wise_list)

        return res


    def is_height_balanced(self, root):
        #check for each subtree(left subtree and right rooted at root) if the diff between left and right node is not more than 1.

        if not root:
            return True, 0

        left_bal, left_h = self.is_height_balanced(root.left)
        right_bal, right_h = self.is_height_balanced(root.right)

        height = 1 + max(left_h, right_h)
        diff = abs(left_h - right_h)
        is_bal = True

        if not left_bal or not right_bal or diff > 1:
            is_bal = False

        return is_bal, height

        # if not root:
        #     return 0
        #
        # left_h = self.is_height_balanced(root.left)
        # if left_h == -1:
        #     return -1
        #
        # right_h = self.is_height_balanced(root.right)
        # if right_h == -1:
        #     return -1
        #
        # diff = abs(left_h - right_h)
        #
        # if diff > 1:
        #     return -1
        #
        # return 1 + max(left_h, right_h)

# btree = BinaryTree()
#
# root = btree.create_tree_from_array([1 ,3 ,5 ,7 ,9])
# btree.inorder(root)
# btree.level_order_traversal(root)
# print
# print btree.depth(root)
# print btree.is_height_balanced(root)
#
# root = TreeNode(5)
# root.left  = TreeNode(7)
# root.right  = TreeNode(12)
#
# root.left.left  = TreeNode(2)
# root.left.right  = TreeNode(11)
# root.right.left  = TreeNode(3)
# root.right.right  = TreeNode(-2)
#
# root.left.left.left  = TreeNode(-3)
# root.left.left.right  = TreeNode(4)
# root.left.left.left  = TreeNode(8)
#
# root.right.left.right  = TreeNode(0)
# root.right.left.right.left  = TreeNode(10)
#
# root.right.right.right  = TreeNode(9)
# root.right.right.right.left  = TreeNode(15)
# root.right.right.right.right  = TreeNode(17)
# root.right.right.right.right.left  = TreeNode(18)
# btree = BinaryTree()
# path1 = []
# btree.get_path(root, 9, path1)
# print path1
# path2 = []
# btree.get_path(root, 15, path2)
# print path2
# print btree.lca(root, 9, 15)
#
# print btree.level_order_traversal(root)
# result = btree.is_height_balanced(root)
# print result
# if result == -1:
#     print "unbalanced"
# else:
#     print "balanced!"
