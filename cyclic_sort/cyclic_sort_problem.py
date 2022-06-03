"""
We are given an array containing n objects. Each object, when created, was assigned a unique number from the range
1 to n based on their creation sequence. This means that the object with sequence number 3 was
created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without using any extra space.
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers,
though each number is actually an object.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):

        number = nums[i]
        number_index = number - 1

        if number == nums[number_index]:

            i += 1

        else:

            nums[i] = nums[number_index]
            nums[number_index] = number

    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
