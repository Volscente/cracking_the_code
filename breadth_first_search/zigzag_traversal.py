"""
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the following levels.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque


class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left, self.right = None, None


def traverse(root):

    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    odd = True

    while queue:

        level_size = len(queue)
        current_level_nodes = deque()

        for _ in range(level_size):

            current_node = queue.popleft()

            if odd:
                current_level_nodes.append(current_node.val)
            else:
                current_level_nodes.appendleft(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        result.append(list(current_level_nodes))
        odd = not odd

    return result


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()