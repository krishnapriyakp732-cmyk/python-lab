def fib_series(n):
    """Return a list of the first n Fibonacci numbers (starting from 0, 1)."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
