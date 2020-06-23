from collections import deque
class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(root):

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
            queue.append((node.left, level+1))

        if node.right:
            queue.append((node.right, level+1))

    if len(level_wise_list) != 0:
        res.append(level_wise_list)
    return res


root = TreeNode(5)
root.left = TreeNode(7)
root.right = TreeNode(12)

root.left.left = TreeNode(2)
root.left.right = TreeNode(11)
root.right.left = TreeNode(3)
root.right.right = TreeNode(-2)

root.left.left.left = TreeNode(-3)
root.left.left.right = TreeNode(4)
root.left.left.left = TreeNode(8)

root.right.left.right = TreeNode(0)
root.right.left.right.left = TreeNode(10)

root.right.right.right = TreeNode(9)
root.right.right.right.left = TreeNode(15)
root.right.right.right.right = TreeNode(17)
root.right.right.right.right.left = TreeNode(18)

print level_order_traversal(root)


