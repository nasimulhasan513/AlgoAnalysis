def powerSum(X, N, num=1):
    val = X - num**N
    if val == 0:
        return 1
    elif val < 0:
        return 0
    else:
        return powerSum(X, N, num + 1) + powerSum(X - num**N, N, num + 1)


X = int(input())
N = int(input())
print(powerSum(X, N))