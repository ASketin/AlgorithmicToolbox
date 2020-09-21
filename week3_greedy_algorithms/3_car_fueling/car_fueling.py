# python3
import sys


def find_nearest_station(current_pos, tank, stops):
    for index, stop in enumerate(stops):
        if stops[index] - stops[index - 1] > tank:
            return None
        if stop > current_pos + tank:
            return index - 1
    return None


def compute_min_refills(distance, tank, stops):
    """
    You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel
    at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
    distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?
    :param distance: integer 1 ≤ 𝑑 ≤ 105.
    :param tank: integer 1 ≤ 𝑚 ≤ 400.
    :param stops: integer 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.
    :return: output the minimum number of refills needed. If it is not possible to
    reach the destination, output −1.
    """
    stops.append(distance)
    current_pos = 0
    index = 0
    refill_number = 0
    while current_pos < distance:
        stops = stops[index:]
        index = find_nearest_station(current_pos, tank, stops)
        if index is None:
            refill_number = refill_number if current_pos + tank >= stops[-1] else -1
            return refill_number
        current_pos = stops[index]
        refill_number += 1


if __name__ == '__main__':

    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
