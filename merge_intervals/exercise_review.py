def insert(intervals, new_interval):

    merged = []
    index = 0

    while index < len(intervals) and intervals[index][1] < new_interval[0]:
        merged.append(intervals[index])
        index += 1

    while index < len(intervals) and intervals[index][0] < new_interval[1]:
        new_interval[0] = min(intervals[index][0], new_interval[0])
        new_interval[1] = max(intervals[index][1], new_interval[1])
        index += 1

    merged.append(new_interval)

    while index < len(intervals):
        merged.append(intervals[index])
        index += 1

    return merged
    

def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()