# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Approach-1
# def missingNumber(nums: list[int]) -> int:
#     for i in range(len(nums) + 1):
#         if i not in nums:
#             return i
#     return 0


# Approach-2
# def missingNumber(nums: list[int]) -> int:
#     currentSum = sum(nums)
#     correctSum = len(nums) * (len(nums) + 1) // 2
#     return correctSum - currentSum
#
#
# num = [0, 2, 3]
# print(missingNumber(num))





