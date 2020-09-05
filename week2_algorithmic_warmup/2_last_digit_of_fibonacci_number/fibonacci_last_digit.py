# Uses python3
import sys


def get_fibonacci_last_digit_naive(num):
    """
    Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
    :param num: The input consists of a single integer 𝑛. 0 ≤ 𝑛 ≤ 107.
    :return: Output the last digit of 𝐹𝑛.
    """
    last_elements = [0, 1]
    for i in range(2, num+1):
        last_elements.append((last_elements[-1] + last_elements[-2]) % 10)
    return last_elements[num]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
