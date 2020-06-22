def fibonacci(i, n, a, b):

    if i == n:
        return b

    c = fibonacci(i+1, n, b, a+b)
    return c

print fibonacci(1, 4, 0, 1)