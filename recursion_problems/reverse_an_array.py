# def reverse_array(arr,left,right):
#     if left>=right:
#         return
#     arr[left], arr[right]= arr[right], arr[left]
#     reverse_array(arr,left+1, right-1)
#     return arr

def reverse_array(arr,i,n):
    if i >= n//2:
        return
    arr[i],arr[n-i-1]= arr[n-i-1],arr[i]
    reverse_array(arr,i+1,n)

input_arr=[10,3,2,67,30,29]
reverse_array(input_arr,0, len(input_arr))
print(input_arr)
# print(reverse_array(input_arr,0,len(input_arr)-1))
