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


def fibonacci_partial_sum_naive(from_, to):
    """
    Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +· · · + 𝐹𝑛.
    :param from_: 0 ≤ 𝑚 ≤ 𝑛 ≤ 1014.
    :param to: 0 ≤ 𝑚 ≤ 𝑛 ≤ 1014.
    :return: Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
    """

    period_list, length = get_period_list(10)
    from_ = from_ % length
    to = (to + 1) % length
    fib_range = range(from_, to)
    if from_ > to:
        f = [x for x in range(from_, length+1)]
        s = [x for x in range(0, to)]
        fib_range = f + s
    last_digit_sum = 0
    for nth in fib_range:
        last_digit_sum = (last_digit_sum + period_list[nth]) % 10
    return last_digit_sum


if __name__ == '__main__':

    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

