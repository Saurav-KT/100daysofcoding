"""There are two arrays A and B. A contains 25 elements whereas, B contains 30 elements. Write a function to create
 an array C that contains only those elements that are common to A and B
 """


# common = []


# Method-1
# def find_common_element(arr1, arr2):
#     for element in arr1:
#         if element in arr2:
#             common.append(element)
#     return common
#
#
# arr_1 = [10, 5, 3, 7, 9, 6]
# arr_2 = [4, 8, 9, 2, 5, 38, 29, 6]
# print(find_common_element(arr_1, arr_2))


def common_elements(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    common = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return common


arr_1 = [4, 8, 9, 2, 5, 38, 29, 6, 18]
arr_2 = [10, 5, 3, 7, 9, 6, 18]
print(common_elements(arr_1, arr_2))

# print(find_common_element(arr_1, arr_2))
