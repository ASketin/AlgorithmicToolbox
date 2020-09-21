#Uses python3

import sys

def max_dot_product(a, b):
    """
    Given two sequences {𝑎1, 𝑎2, . . . , 𝑎𝑛} and {𝑏1, 𝑏2, . . . , 𝑏𝑛}, we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗)
    such that the sum of their products is maximized.
    :param a: 𝑎𝑖 is the profit per click of the 𝑖-th ad
    :param b: 𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot
    :return: Output the maximum value of permutation
    """
    a.sort()
    b.sort()
    res = 0
    for a_i, b_i in zip(a, b):
        res += a_i * b_i
    return res


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
