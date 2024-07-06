def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        if left_sum == (total_sum - left_sum - num):
            return "YES"
        left_sum += num
        
    return "NO"

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(balancedSums(arr))