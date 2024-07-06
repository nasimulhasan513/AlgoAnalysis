def pickingNumbers(a):
    a.sort()
    max_count = 0
    for i in range(len(a)):
        count = 0
        for j in range(i, len(a)):
            if abs(a[i] - a[j]) <= 1:
                count += 1
        if count > max_count:
            max_count = count
    return max_count


n = int(input())
a = list(map(int, input().split()))
print(pickingNumbers(a))
