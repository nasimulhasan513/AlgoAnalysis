def missingNumbers(arr, brr):
    arr_count = {}
    brr_count = {}
    

    for num in arr:
        if num in arr_count:
            arr_count[num] += 1
        else:
            arr_count[num] = 1
    

    for num in brr:
        if num in brr_count:
            brr_count[num] += 1
        else:
            brr_count[num] = 1
    

    missing = []
    for num in brr_count:
        if num not in arr_count or brr_count[num] != arr_count[num]:
            missing.append(num)
        
    return sorted(missing)


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

m = int(input().strip())

brr = list(map(int, input().rstrip().split()))

result = missingNumbers(arr, brr)

print(' '.join(map(str, result)))
 