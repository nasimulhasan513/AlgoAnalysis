for _ in [0]*int(input()):
    N = int(input().strip())
    print((2 + pow(2,N+1)) % (10**9 + 7))
