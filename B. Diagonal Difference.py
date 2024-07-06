def diagonalDifference(arr):
    l = len(arr)
    return abs(sum(arr[i][i] - arr[i][l-i-1] for i in range(l)))

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
print(diagonalDifference(arr))