def compute_sum_of_square(num):

    num_list = [int(x) for x in str(num)]

    num_square_list = [x * x for x in num_list]

    return sum(num_square_list)

def find_happy_number(num):

    slow, fast = num, num

    while fast != 1:

        slow = compute_sum_of_square(slow)
        fast = compute_sum_of_square(compute_sum_of_square(fast))

        if slow == fast:

            return False
        
    return True


print(find_happy_number(12))
print(find_happy_number(23))