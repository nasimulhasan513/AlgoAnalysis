def closestNumbers(arr):
    arr.sort()
    min_diff = float('inf')
    result = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i - 1], arr[i]]
        elif diff == min_diff:
            result.extend([arr[i - 1], arr[i]])
    return result

n = input()
arr = list(map(int, input().split()))
result = closestNumbers(arr)
print(' '.join(map(str, result)))
    
