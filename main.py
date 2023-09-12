

def reverse_string(string):
    return string[::-1]


def largest_of_three(x, y, z):
    return max([x, y, z])


def factorial(x: int):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def fib_sequence(x: int):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fib_sequence(x - 1) + fib_sequence(x - 2)

