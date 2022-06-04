"""
Given a binary tree and a number ‘S’,
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

Time Complexity: O(N^2)
Space Complexity: O(NlogN)
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_paths(root):

    all_paths = []

    compute_path_recursive(root, [], all_paths)

    return all_paths


def compute_path_recursive(current_node, current_path, all_paths):

    if current_node is None:
        return False

    current_path.append(current_node.val)

    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        compute_path_recursive(current_node.left, current_path, all_paths)
        compute_path_recursive(current_node.right, current_path, all_paths)

    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths " + str(get_all_paths(root)))


main()
