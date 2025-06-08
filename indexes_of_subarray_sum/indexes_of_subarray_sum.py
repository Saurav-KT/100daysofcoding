"""Given an array arr[] containing only non-negative integers,
your task is to find a continuous subarray (a contiguous sequence of elements)
whose sum equals a specified value target. You need to return the 1-based indices of
the leftmost and rightmost elements of this subarray. You need to find the first subarray
whose sum is equal to the target.

Note: If no such array is possible then, return [-1]."""

class Solution:
    def subarraySum(self, arr, target):
        # code here
       left = 0
       current_sum = 0

       for right in range(len(arr)):
            current_sum += arr[right]

            while current_sum >= target:
                  if current_sum == target:
                       return [left + 1, right + 1]
                  current_sum-= arr[left]
                  left+=1
       return [-1]

lst=[1, 2, 3, 7, 5]
t=12
obj= Solution()
print(obj.subarraySum(lst,t))