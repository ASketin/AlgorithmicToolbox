# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    """
    Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
    :param n: 1 ≤ 𝑛 ≤ 10^14
    :param m: 2 ≤ 𝑚 ≤ 10^3
    :return: Output 𝐹𝑛 mod 𝑚.
    """

    not_found_period = True
    period_list = [0, 1]
    if n < len(period_list):
        return period_list[n]
    while not_found_period:
        for i in range(1, n):
            period_list.append((period_list[-1] + period_list[-2]) % m)
            if period_list[-1] == 0 and period_list[-2] == 1:
                not_found_period = False
                n = n % (len(period_list) - 1)
                break

    return period_list[n]


if __name__ == '__main__':

    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))