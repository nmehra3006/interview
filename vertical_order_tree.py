from collections import defaultdict
from collections import deque

class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_order(root):

    if not root:
        return []

    q = deque([(root, (0, 0))])

    col_map = defaultdict(list)

    while q:

        next_node, (row, col) = q.popleft()

        col_map[col].append((row, next_node.val))

        if next_node.left:
            q.append((next_node.left, (row+1, col-1)))

        if next_node.right:
            q.append((next_node.right, (row + 1, col + 1)))

    for sorted_key in sorted(col_map.keys()):
        for row, val in col_map[sorted_key]:
            print val


root = TreeNode(5)
root.left  = TreeNode(7)
root.right  = TreeNode(12)

root.left.left  = TreeNode(2)
root.left.right  = TreeNode(11)
root.right.left  = TreeNode(3)
root.right.right  = TreeNode(-2)

root.left.left.left  = TreeNode(-3)
root.left.left.right  = TreeNode(4)

root.right.left.right  = TreeNode(0)
root.right.left.right.left  = TreeNode(10)

root.right.right.right  = TreeNode(9)
root.right.right.right.left  = TreeNode(15)
root.right.right.right.right  = TreeNode(17)
root.right.right.right.right.left  = TreeNode(18)

vertical_order(root)

