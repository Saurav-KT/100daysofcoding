class Solution:
    # Function to rotate an array by d elements in counter-clockwise or left direction.
    # Approach-1 The rotation algorithm runs in linear time O(n) with constant extra space O(1).
    def rotate_arr(self, arr, d):
        def reverse(left: int, right: int):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(arr)

        # Handle the case where d > size of array
        d = d % n

        # Reverse the first d elements
        reverse(0, d - 1)

        # Reverse the remaining n-d elements
        reverse(d, n - 1)

        # Reverse the entire array
        reverse(0, n - 1)
        # print(arr)

    '''Approach-2 Time complexity O(n*d), the outer loop runs d times, and within each iteration, the inner 
    loop shifts all n elements of the array by one position, 
    resulting in a total of n*d operations.'''

    def rotate_left(self, arr, d):
        n = len(arr)
        for i in range(d):
            first = arr[0]
            for j in range(n - 1):
                arr[j] = arr[j + 1]
            arr[n - 1] = first
        return arr




if __name__ =="__main__":
    # arr1=[1,2,3]
    # k= 4
    obj= Solution()
    # obj.rotate_arr( arr1, k)

    arr2 = [1, 2, 3, 4, 5, 6]
    k = 2
    print(obj.rotate_left(arr2, k))

