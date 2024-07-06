arr = list(map(int, input().split()))
arr.sort()

min_sum = sum(arr[:-1])
max_sum = sum(arr[1:])

print(min_sum, max_sum)