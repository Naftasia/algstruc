def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1] 
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quicksort(left) + middle + quicksort(right)

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = quicksort(arr)
print(" ".join(map(str, sorted_arr)))
