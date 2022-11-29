def merge_two_sorted_array(lst1, lst2):
    count_list1 = len(lst1)
    count_list2 = len(lst2)
    arr = []
    i, j = 0, 0
    while i < count_list1 and j < count_list2:
        if lst1[i] < lst2[j]:
            arr.append(lst1[i])
            i += 1
        else:
            arr.append(lst2[j])
            j += 1

    arr = arr + lst1[i:] + lst2[j:]
    return arr


lst1 = [1, 4, 10, 15]
lst2 = [1, 3, 5, 40, 50, 60]
print(merge_two_sorted_array(lst1, lst2))
