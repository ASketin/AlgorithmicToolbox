import sys


def greater_or_equal(digit_1, digit_2):
    return int(digit_1 + digit_2) >= int(digit_2 + digit_1)


def largest_number(a):
    """
    Compose the largest number out of a set of integers.
    :param a: integers 𝑎1, 𝑎2, . . . , 𝑎𝑛. 1 ≤ 𝑎𝑖 ≤ 10^3
    :return: Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
    """
    res = ""
    while a:
        max_digit = '0'
        for digit in a:
            if greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
