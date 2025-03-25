def selection_sort_count(arr):
    n = len(arr)
    first_element = arr[0]  
    first_element_position = 0 
    first_element_moves = 0 

    for i in range(n):
        min_index = i 

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        

        if min_index != i:

            if i == first_element_position or min_index == first_element_position:
                first_element_moves += 1

            arr[i], arr[min_index] = arr[min_index], arr[i]

            if first_element_position == i:
                first_element_position = min_index

            elif first_element_position == min_index:
                first_element_position = i

    return first_element_moves

n = int(input())
arr = list(map(int, input().split())) 

result = selection_sort_count(arr)

print(result)
