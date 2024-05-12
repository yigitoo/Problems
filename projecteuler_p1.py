def solve(n: int = 1000):
    l: list[int] = list()

    for i in range(1, n):
        if i % 15 == 0:
            l.append(i)
        elif i % 3 == 0:
            l.append(i)
        elif i % 5 == 0:
            l.append(i)

    print(l)
    return sum(l)

result = solve()
print(result)
