from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):

        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):

        return self.x * self.x + self.y * self.y


def main():

    points = [Point(2, 2), Point(3, 3), Point(1, 1), Point(4, 4,)]

    max_heap = []

    for point in points:

        heappush(max_heap, point)

    for point in max_heap:
        print(point.x)
        print(point.y)
        print('\n')


main()