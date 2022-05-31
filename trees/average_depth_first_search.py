"""
Problem description:
Return the average of the node's values at each depth level in a Binary Tree.

        4
       | \
      6   10
     | \   \
    3   4   11
              \
               4

output: [4, 8, 6, 4]

avg_by_depth
1 - 4
{0: [4]}

2 - 6
{0: [4], 1: [6]}

3 - 3
{0: [4], 1: [6], 2: [3]}

4 -
None

5 - 4
{0: [4], 1: [6], 2: [3, 4]}

6 -
None

7 - 10
{0: [4], 1: [6, 10], 2: [3, 4]}

8 -
None

9 - 11
{0: [4], 1: [6, 10], 2: [3, 4, 11]}

10 -
None

11 - 4
{0: [4], 1: [6, 10], 2: [3, 4, 11], 3: []4}

12 -
None

13 - None
"""


class Node:

    def __init__(self, value):

        self.value = value
        self.left_child = None
        self.right_child = None


def _breadth_first_search(node, dict, depth=0):

    if node is None:

        return None

    if depth not in dict.keys():

        dict[depth] = []

    dict[depth].append(node.value)

    _breadth_first_search(node.left_child, dict, depth + 1)
    _breadth_first_search(node.right_child, dict, depth + 1)


def avg_by_depth(node):

    avg_dict = {}
    output = []

    _breadth_first_search(node, avg_dict)

    for depth in avg_dict.keys():

        depth_sum = sum(avg_dict[depth])
        avg = depth_sum / len(avg_dict[depth])
        output.append(int(avg))

    print(avg_dict)
    print(output)


if __name__ == '__main__':

    node_root = Node(4)
    node_1 = Node(6)
    node_2 = Node(10)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(11)
    node_6 = Node(4)

    node_root.left_child = node_1
    node_root.right_child = node_2
    node_1.left_child = node_3
    node_1.right_child = node_4
    node_2.right_child = node_5
    node_5.right_child = node_6

    avg_by_depth(node_root)


