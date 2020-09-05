# Uses python3
import sys


def gcd_naive(first: int, second: int):
    """
    Given two integers 𝑎 and 𝑏, find their greatest common divisor.
    :param first: input integer 1 ≤ 𝑎 ≤ 2 · 10^9.
    :param second: input integer 1 ≤ 𝑏 ≤ 2 · 10^9.
    :return: Output GCD(𝑎, 𝑏).
    """
    if first < second:
        tmp = first
        first = second
        second = tmp

    while second != 0:
        tmp = first
        first = second
        second = tmp % second

    return first


def lcm_naive(g, d):
    """
    Given two integers 𝑎 and 𝑏, find their least common multiple.
    :param g: integer 1 ≤ g ≤ 107.
    :param d: integer 1 ≤ d ≤ 107.
    :return: Output the least common multiple of 𝑎 and 𝑏.
    """
    return d * (g // gcd_naive(g, d))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))