n = int(input())
words = [input() for _ in range(n)]  

# Алгоритм сортування вибором
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if words[j] < words[min_index]:
            min_index = j
    words[i], words[min_index] = words[min_index], words[i]

for word in words:
    print(word)
