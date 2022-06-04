"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
i.e., the lowest level comes first.
You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:

        level_size = len(queue)
        current_level_nodes = []

        for _ in range(level_size):

            current_node = queue.popleft()
            current_level_nodes.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        result.appendleft(current_level_nodes)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
