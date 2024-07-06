def angryProfessor(k, a):
    on_time_students = sum(1 for time in a if time <= 0)
    return "YES" if on_time_students < k else "NO"

n = int(input())
for _ in range(n):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(angryProfessor(k, a))