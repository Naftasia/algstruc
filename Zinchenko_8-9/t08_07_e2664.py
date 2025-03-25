n = int(input()) 
arr = list(map(int, input().split()))

# Алгоритм сортування вставкою
for i in range(1, n):
    key = arr[i]
    j = i - 1
    original = arr[:]
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key
    if arr != original:
        print(" ".join(map(str, arr)))
