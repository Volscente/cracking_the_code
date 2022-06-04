"""
Find the largest value on each level of a binary tree.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_max_level_node(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:

        level_size = len(queue)
        max_level_node = 0

        for _ in range(level_size):

            current_node = queue.popleft()
            max_level_node = max(max_level_node, current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        result.append(max_level_node)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level max are: " + str(find_max_level_node(root)))


main()
