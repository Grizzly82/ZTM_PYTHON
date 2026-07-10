#Creating a fibonacci sequence in a list using list comprehension


def fib_seq(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for i in range(n-2)]
    return fib

print(fib_seq(20))