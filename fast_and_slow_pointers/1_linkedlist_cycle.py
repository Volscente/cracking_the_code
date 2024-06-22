"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    """
    Time Complexity: O(N)
    Space Complexity O(1)
    :param head:
    :return:
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head))) # False

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head))) # True

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head))) # True


main()
