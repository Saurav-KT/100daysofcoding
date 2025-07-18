def reverse_array(arr,left,right):
    if left>=right:
        return
    arr[left], arr[right]= arr[right], arr[left]
    reverse_array(arr,left+1, right-1)
    return arr

input_arr=[10,3,2,67,30,29]
print(reverse_array(input_arr,0,len(input_arr)-1))