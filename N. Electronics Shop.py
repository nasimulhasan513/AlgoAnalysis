def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                max_spent = max(max_spent, k + d)
    return max_spent

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

print(getMoneySpent(keyboards, drives, b))
