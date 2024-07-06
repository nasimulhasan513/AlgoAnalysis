def decentNumber(n):
    fives = n
    while fives % 3 != 0:
        fives -= 5
    if fives < 0:
        return -1
    else:
        threes = n - fives
        return '5' * fives + '3' * threes
    
for _ in range(int(input())):
    n = int(input())
    print(decentNumber(n))