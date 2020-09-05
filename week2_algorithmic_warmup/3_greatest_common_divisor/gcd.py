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


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
    """
    print(gcd_naive(18, 35))
    print(gcd_naive(28851538, 1183019))
    """