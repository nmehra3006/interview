class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def arr_to_bst(root, node):

    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            arr_to_bst(root.left, node)

    else:
        if root.right is None:
            root.right = node
        else:
            arr_to_bst(root.right, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

r = TreeNode(50)
arr_to_bst(r, TreeNode(30))
arr_to_bst(r, TreeNode(20))
arr_to_bst(r, TreeNode(40))
arr_to_bst(r, TreeNode(70))
arr_to_bst(r, TreeNode(60))
arr_to_bst(r, TreeNode(80))
inorder(r)