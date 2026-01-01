'''Given an integer array nums, rotate the array
to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''

def rotate_arr(arr, k):
    def reverse(left: int, right: int):
        while left < right:
            arr[left], arr[right]= arr[right], arr[left]
            left+=1
            right-=1

    n= len(arr)
    k= k % n
    reverse(0, n-1)
    reverse(0,k-1)
    reverse(k, n-1)
    print(arr)

def rotate_array(arr, d):
    n= len(arr)

    # Repeat the rotation d times
    for _ in range(d):
        # Right rotate the array by one position
        last = arr[n - 1]
        for i in range(n-1,0,-1):
            arr[i]= arr[i-1]
        arr[0]= last
    print(arr)


if __name__== "__main__":
    # arr=[1,2,3,4,5,6,7]
    # k=3
    # rotate_arr(arr, k)

    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    rotate_array(arr, d)

