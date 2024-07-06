def beautifulPairs(A, B):
    freq_A = {}
    freq_B = {}
    
    for num in A:
        if num in freq_A:
            freq_A[num] += 1
        else:
            freq_A[num] = 1
    
    for num in B:
        if num in freq_B:
            freq_B[num] += 1
        else:
            freq_B[num] = 1
    
    initial_pairs = 0
    for num in freq_A:
        if num in freq_B:
            initial_pairs += min(freq_A[num], freq_B[num])
    

    max_pairs = initial_pairs
    
    if initial_pairs == len(A):
        max_pairs -= 1
    else:
        max_pairs += 1
    
    return max_pairs


n = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(beautifulPairs(A, B))
