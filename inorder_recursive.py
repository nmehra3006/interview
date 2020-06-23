class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root , result):

    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
res = []
inorder(root, res)
print res

# res is global
# res as a list in function using extend 