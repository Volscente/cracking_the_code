"""
Given a binary tree, find the root-to-leaf path with the maximum sum.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_path_max_sum(root):
    max_sum = 0
    path_max_sum = []

    compute_path_sum(root, [], max_sum, 0, path_max_sum)

    return path_max_sum, max_sum


def compute_path_sum(current_node, current_path, max_sum, path_sum, path_max_sum):

    if current_node is None:
        return False

    print('Node: ' + str(current_node.val))

    current_path.append(current_node.val)
    path_sum += current_node.val

    if current_node.left is None and current_node.right is None and path_sum > max_sum:
        max_sum = path_sum
        path_max_sum = current_path.copy()
    else:
        compute_path_sum(current_node.left, current_path, max_sum, path_sum, path_max_sum)
        compute_path_sum(current_node.right, current_path, max_sum, path_sum, path_max_sum)
    del current_path[-1]

    print(path_max_sum)
    print('Max sum: ' + str(max_sum))


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths " + str(get_path_max_sum(root)))


main()