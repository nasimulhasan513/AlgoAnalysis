def hurdleRace(k, height):
    max_height = max(height)
    return max(0, max_height - k)

n,k = map(int,input().split())
height = list(map(int,input().split()))
print(hurdleRace(k, height))
