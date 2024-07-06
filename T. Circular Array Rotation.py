def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n  # Effective rotations
    rotated_array = a[-k:] + a[:-k]
    return [rotated_array[q] for q in queries]

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

q = int(first_multiple_input[2])

a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)
print('\n'.join(map(str, result)))