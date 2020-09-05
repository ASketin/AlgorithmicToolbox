# Uses python3


def calc_fib(num: int):
    """
    Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
    :param num: The input consists of a single integer 𝑛. 0 ≤ 𝑛 ≤ 45.
    :return: Output 𝐹𝑛.
    """
    last_elements = [0, 1]
    for i in range(2, num+1):
        last_elements.append(last_elements[-1] + last_elements[-2])
    return last_elements[num]


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))