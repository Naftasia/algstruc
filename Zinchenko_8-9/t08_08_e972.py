n = int(input())
times = []

for _ in range(n):
    h, m, s = map(int, input().split())
    times.append((h, m, s))

times.sort()

for time in times:
    print(time[0], time[1], time[2])
