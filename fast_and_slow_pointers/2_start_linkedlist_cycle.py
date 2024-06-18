from __future__ import print_function

"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.



If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:

1. Take two pointers. Let’s call them pointer1 and pointer2.

2. Initialize both pointers to point to the start of the LinkedList.

3. We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle. 
Let’s assume that the length of the cycle is ‘K’ nodes.

4. Move pointer2 ahead by ‘K’ nodes.

5. Now, keep incrementing pointer1 and pointer2 until they both meet.

6 As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. 
Their meeting point will be the start of the cycle.


Time Complexity:
    - Finding cycle is O(N)
    - Calculate cycle length is O(N)
    - Find the starting point is O(N)
        - Total: O(N)
        
Space Complexity: O(1)
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            return calculate_cycle_length(slow)


def calculate_cycle_length(slow):

    current = slow
    cycle_length = 0

    while True:

        current = current.next
        cycle_length += 1

        if current == slow:

            break

    return cycle_length


def find_cycle_start(head):

    cycle_length = find_cycle(head)

    pointer_1 = head
    pointer_2 = head

    for i in range(cycle_length):
        pointer_2 = pointer_2.next

    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
    return pointer_1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
