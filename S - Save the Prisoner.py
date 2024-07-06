def saveThePrisoner(n, m, s):
    return ((s - 1 + m - 1) % n) + 1

n = int(input())
for _ in range(n):
    n, m, s = map(int, input().split())
    print(saveThePrisoner(n, m, s))
