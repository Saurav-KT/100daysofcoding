# Problem statement
# Find a non repetitive element from an array
# Approach-1
# arr_item = [2, 3, 2, 4, 2, 6, 4, 8, 10, 6, 39, 8]


# distinct_item = set(arr_item)
# for i in distinct_item:
#     x = [element for element in arr_item if element == i]
#     if x.count(i) == 1:
#         print(i)

# Approach-2
def find_duplicate(arr, n):
    for i in range(n):
        j = 0
        while j < n:
            if arr[i] == arr[j] and i != j:
                break
            j += 1
        if j == n:
            print(arr[i])


arr_item = [2, 3, 2, 4, 2, 6, 4, 8, 10, 6, 39, 8]
find_duplicate(arr_item,len(arr_item))