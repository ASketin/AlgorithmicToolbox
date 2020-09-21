# Uses python3
import sys


def optimal_summands(n):
    """
    The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
    𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
    :param n: 1 ≤ 𝑛 ≤ 109.
    :return: In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
    of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
    that sum up to 𝑛 (if there are many such representations, output any of them).
    """
    prizes = []
    rsd = n
    if n == 1:
        return [1]
    for i in range(1, n):
        if rsd > 2*i:
            prizes.append(i)
            rsd -= i
        else:
            prizes.append(rsd)
            break
    return prizes


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
