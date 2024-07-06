def migratoryBirds(arr):
    bird_count = {}
    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1
    
    max_frequency = max(bird_count.values())
    
    most_frequent_birds = [bird for bird, count in bird_count.items() if count == max_frequency]
    return min(most_frequent_birds)


n = input()
arr = list(map(int, input().split()))
print(migratoryBirds(arr))

