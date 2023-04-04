# TASK 1

def sumOfRange(n):
    if not isinstance(n, int):
        raise TypeError
    if not (1 <= n <= 10 ** 25):
        raise ValueError

    return n * (n + 1) / 2