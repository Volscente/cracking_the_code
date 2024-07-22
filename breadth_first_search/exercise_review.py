from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse(root):

    results = []

    if root is None:

        return results
    
    queue = deque()
    queue.append(root)

    while queue:

        level_size = len(queue)

        level_nodes = []

        for _ in range(level_size):

            current_node = queue.popleft()
            level_nodes.append(current_node.val)

            if current_node.left:

                queue.append(current_node.left)

            if current_node.right:

                queue.append(current_node.right)

        results.append(level_nodes)

    return results

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()