"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

See README.md for more details

Time Complexity: O(logN)
Space Complexity: O(1)
"""


def find_happy_number(num):

    slow = num
    fast = num

    while fast != 1:

        slow = calculate_sum_of_square(slow)
        fast = calculate_sum_of_square(calculate_sum_of_square(fast))

        if slow == fast:

            return False

    return True


def calculate_sum_of_square(num):

    num_list = [int(x) for x in str(num)]

    num_squared_list = [x * x for x in num_list]

    return sum(num_squared_list)


def main():

    print(find_happy_number(23))
    print(find_happy_number(12))


main()