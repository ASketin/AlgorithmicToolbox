# Uses python3
import sys


def get_period_list(m):
    """
    Given 𝑚, output period for mod m.
    :param m: integer
    :return: period list and length of it
    """

    not_found_period = True
    period_list = [0, 1]
    while not_found_period:
        period_list.append((period_list[-1] + period_list[-2]) % m)
        if period_list[-1] == 0 and period_list[-2] == 1:
            not_found_period = False
            break

    return period_list, len(period_list) - 1


def fibonacci_sum_naive(n):
    """
    Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
    :param n: The input consists of a single integer 𝑛. 0 ≤ 𝑛 ≤ 1014.
    :return: Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
    """
    last_digit_sum = 0
    period_list, length = get_period_list(10)
    period_pos = n % length
    for nth in range(1, period_pos + 1):
        last_digit_sum = (last_digit_sum + period_list[nth]) % 10
    return last_digit_sum


if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
