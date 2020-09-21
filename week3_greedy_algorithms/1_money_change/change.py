# Uses python3
import sys


def get_change(m):
    """
        The goal in this problem is to find the minimum number of coins needed to change the input value
        (an integer) into coins with denominations 1, 5, and 10.
    :param m: 1 ≤ 𝑚 ≤ 103.
    :return: Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
    """
    coins = (1, 5, 10)
    amount = 0
    for coin in coins[::-1]:
        while m >= coin:
            m = m - coin
            amount += 1

    return amount


if __name__ == '__main__':

    m = int(sys.stdin.read())
    print(get_change(m))