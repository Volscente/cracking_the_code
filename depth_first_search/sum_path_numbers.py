class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    all_paths = []

    compute_all_paths(root, [], all_paths)

    return all_paths


def compute_all_paths(current_node, current_path, all_paths):
    if current_node is None:
        return False

    current_path.append(current_node.val)

    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        compute_all_paths(current_node.left, current_path, all_paths)
        compute_all_paths(current_node.right, current_path, all_paths)
    del current_path[-1]


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
