def get_product_array(arr):
    n = len(lst)
    left, right = [1] * n, [1] * n
    product_array = []
    # buid left hand array
    for i in range(1,n):
        left[i]= left[i-1]* arr[i-1]

    # build right hand array
    for i in range(1,n):
        right[i]= right[i-1]* arr[::-1][i-1]

    #build product array from subarray
    for i in range(n):
        product_array.append(left[i]* right[::-1][i])
    return product_array

lst = [10, 3, 7, 2, 6]
output = [252, 840, 360, 1260, 420]
print(get_product_array(lst))

