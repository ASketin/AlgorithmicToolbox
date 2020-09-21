# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """
    The goal of this code problem is to implement an algorithm for the fractional knapsack problem
    :param capacity: 0 ≤ 𝑊 ≤ 2
    :param weights: 0 < 𝑤𝑖 ≤ 2 · 106
    :param values: 0 ≤ 𝑣𝑖 ≤ 2 · 106
    :return: Output the maximal value of fractions of items that fit into the knapsack.
    """
    value = 0.

    values = [(value / weight, weight) for value, weight in zip(values, weights)]
    values.sort()
    for price, weight in values[::-1]:
        weight = weight if weight < capacity else capacity
        tmp = price * weight
        capacity -= weight
        value += tmp
        if capacity == 0:
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
