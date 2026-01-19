
# output=[19,20,36]


def sort_arr(arr: list):
    if len(arr)<=1:
        return
    temp= arr[-1]
    arr.pop()
    sort_arr(arr)
    insert(arr, temp)
    return arr

def insert(arr: list, temp):
    if len(arr)==0 or arr[-1]<= temp:
        arr.append(temp)
        return
    val = arr[len(arr)-1]
    arr.pop()
    insert(arr, temp)
    arr.append(val)
    return

arr=[20,36,19, 46]
print(sort_arr(arr))
