def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    while left and right:
        if len(left[0]) < len(right[0]) or (len(left[0]) == len(right[0]) and left[0] < right[0]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged

n = int(input())
unsorted = [input() for _ in range(n)]

sorted_list = merge_sort(unsorted)
print("\n".join(sorted_list))
