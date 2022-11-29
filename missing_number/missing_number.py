# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

def missingNumber(nums: list[int]) -> int:
    n = len(nums) + 1
    if 1 <= n <= pow(10, 4):
        for i in range(n):
            if i not in nums:
                return i
        return 0


num = [0, 1]
print(missingNumber(num))
