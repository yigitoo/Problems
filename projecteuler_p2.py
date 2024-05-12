
cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:  # Base case
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)  # Recursive case
    return cache[n]

def solve(n = 4_000_000):
    _fib: list[int] = [fib(n) for n in range(50)]
    res = []

    while True:
        if _fib[-1] > n:
            _fib.pop()
        else:
            break

    for num in _fib:
        if num % 2 == 0:
            res.append(num)
    print(_fib)
    print(res)
    return sum(res)


result = solve()
print(result)
