"""
Given a binary tree and a number ‘S’,
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

Time Complexity: O(N^2) -> Fetch all the nodes and the paths
Space Complexity: O(N * logN) -> Space needed to store All Paths -> In a Binary Tree there could be at most (N + 1)/2 leaves.
Where N is the number of nodes. The length of a path can be at most logN so O(N + 1)/2 = O(N) and O(logN) -> O(N) * (logN)
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_paths(root, sum_value):
    all_paths = []

    find_all_paths_recursive(root, sum_value, [], all_paths)

    return all_paths


def find_all_paths_recursive(current_node, sum_value, current_path, all_paths):
    if current_node is None:
        return False

    current_path.append(current_node.val)

    if current_node.val == sum_value and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        find_all_paths_recursive(current_node.left, sum_value - current_node.val, current_path, all_paths)
        find_all_paths_recursive(current_node.right, sum_value - current_node.val, current_path, all_paths)

    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(get_all_paths(root, sum)))


main()
