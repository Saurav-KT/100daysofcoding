# Problem statement: find the number which is repeated a maximum number of times.

def find_max_occurrence(arr, n):
    maxcount = 0
    frequent_occurred_element = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count > maxcount:
            maxcount = count
            frequent_occurred_element = arr[i]
    return frequent_occurred_element


arr = [40, 50, 30, 40, 50, 30, 30, 30]
print(find_max_occurrence(arr, len(arr)))
