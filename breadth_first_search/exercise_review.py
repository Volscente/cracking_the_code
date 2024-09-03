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

    reverse = False

    while queue:

        current_level_length = len(queue)

        current_level_nodes = deque()

        for i in range(current_level_length):

            current_node = queue.popleft()

            print(current_node.val)

            if reverse:

                current_level_nodes.appendleft(current_node.val)

            else:

                current_level_nodes.append(current_node.val)

            if current_node.left:

                queue.append(current_node.left)

            if current_node.right:

                queue.append(current_node.right)

        reverse = not reverse

        result.append(current_level_nodes)

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