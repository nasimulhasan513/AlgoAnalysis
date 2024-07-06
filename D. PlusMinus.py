def plus_minus(arr):
    n = len(arr)
    positive = len([x for x in arr if x > 0]) / n
    negative = len([x for x in arr if x < 0]) / n
    zero = len([x for x in arr if x == 0]) / n
    
    print(f"{positive:.6f}")
    print(f"{negative:.6f}")
    print(f"{zero:.6f}")

n = input()
arr = list(map(int, input().split()))
plus_minus(arr)