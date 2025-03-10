# Given an array of integers of size ‘n’,
# Our aim is to calculate the maximum sum of ‘k’ consecutive elements in
# the array

def max_sum(arr, k):
    arr_length = len(arr)
    if arr_length < k:
        print("invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(arr_length - k + 1):
        window_sum = sum(arr[i:i + k])
        max_sum = max(window_sum, max_sum)

    return max_sum


lst = [1, 4, 2, 10, 2, 3, 1, 0]
k = 3
max_sum(lst, k)

# print(arr[::-1])
# window_sum= sum(arr[::k])
# print(window_sum)
