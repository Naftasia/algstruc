def digit_sum(x):
    return sum(map(int, str(x)))

def sort_numbers_by_weight(n):
    numbers = list(range(1, n + 1))
    numbers.sort(key=lambda x: (digit_sum(x), str(x)))
    return numbers

def find_kth_number_position(numbers, k):
    return numbers.index(k) + 1

n = int(input())
k = int(input())

sorted_numbers = sort_numbers_by_weight(n)

print(find_kth_number_position(sorted_numbers, k))
print(sorted_numbers[k - 1])
