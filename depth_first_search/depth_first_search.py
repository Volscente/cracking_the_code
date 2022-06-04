class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth_first_search(root):
    if root is None:
        return None

    print(root.val)

    depth_first_search(root.left)
    depth_first_search(root.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    depth_first_search(root)


main()