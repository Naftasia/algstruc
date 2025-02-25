
# Функція для пошуку лівої межі (першого входження)
def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

# Функція для пошуку правої межі (першого елементу, який більший за x)
def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

# Зчитуємо вхідні дані
n = int(input()) 
arr = list(map(int, input().split()))
m = int(input()) 
queries = list(map(int, input().split()))

# Для кожного запиту обчислюємо кількість звіряток цього кольору
for query in queries:
    left = lower_bound(arr, query)
    right = upper_bound(arr, query)
    print(right - left)
