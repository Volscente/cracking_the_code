"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""

from heapq import *


class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    """
    Time Complexity: O(N*logK)
    Space Complexity: O(K)
    :param lists:
    :return:
    """
    min_heap = []

    # O(K * logK)
    for head in lists:
        heappush(min_heap, head)

    result_head, result_tail = None, None

    # O((N-K) * (logK + logK))
    while min_heap:

        node = heappop(min_heap)

        if result_head is None:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        if node.next is not None:
            heappush(min_heap, node.next)

    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
