"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):

    # Nothing to reverse
    if p == q:

        return head

    i = 0
    previous, current = None, head

    # Navigate to the 'p' node
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # Set pointers for the last assign
    last_node_first_sequence = previous
    last_node_sub_sequence = current

    i = 0
    next_node = None

    # Reverse the subsequence
    while current is not None and i < q - p + 1:

        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        i += 1

    # Final assign
    if last_node_first_sequence is not None:
        last_node_first_sequence.next = previous

    else:

        head = previous

    last_node_sub_sequence.next = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
