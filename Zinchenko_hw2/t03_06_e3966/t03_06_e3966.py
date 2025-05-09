import bisect

n = int(input())
collection = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for k in queries:
    idx = bisect.bisect_left(collection, k)
    if idx < n and collection[idx] == k:
        print("YES")
    else:
        print("NO")
