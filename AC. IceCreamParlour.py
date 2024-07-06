def icecreamChoices(total_amount, cost_list):
    index_map = {}
    for idx, cost in enumerate(cost_list):
        needed_cost = total_amount - cost
        if needed_cost in index_map:
            return [index_map[needed_cost] + 1, idx + 1]
        index_map[cost] = idx

for _ in range(int(input())):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(map(str, icecreamChoices(m, arr))))


