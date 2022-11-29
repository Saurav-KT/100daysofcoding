# Check if two arrays are equal or not
# Approach: Sorting the array: Sort both the arrays and in a single traversal compare their values at each index.
# Time Complexity: O(n log n) using merge sort.
# Space Complexity: O(1)

def check_two_arrays_are_equal(arr_1, arr_2):
    if len(arr_1) != len(arr_2):
        return False
    arr_1 = sorted(arr_1)
    arr_2 = sorted(arr_2)
    for element in range(len(arr_1)):
        if arr_1[element] != arr_2[element]:
            return False
    return True


arr_obj1 = [3, 8, 9, 1]
arr_obj2 = [9, 3, 1, 8]
print(check_two_arrays_are_equal(arr_obj1, arr_obj2))
