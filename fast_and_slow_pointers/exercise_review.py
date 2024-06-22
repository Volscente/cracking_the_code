class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def compute_square(num):

    num_list = [int(x) for x in str(num)]

    square_list = [x * 2 for x in num_list]

    return sum(square_list)

def find_happy_numer(num):

    slow, fast = num, num

    while fast != 1:

        slow = compute_square(slow)
        fast = compute_square(compute_square(fast))

        if slow == fast:

            return False

def main():
    pass


main()