# Method-1
def reverse_array(arr):
    output=[]
    for i in range(len(arr)-1,-1,-1):
        output.append(arr[i])
    return output

arr=[1,3,8,9,20,60]
print(reverse_array(arr))

# Method-2
# arr= arr[::-1]
# print(arr)

def reverse_arr(arr):
    left=0
    right=len(arr)-1
    while left< right:
        arr[left], arr[right]= arr[right],arr[left]
        left+=1
        right-=1
    return arr

