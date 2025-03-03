# Given an integer array nums, move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]

class Solution:
    def movezeros(self, nums: list[int])->None:
        slow=0
        for fast in range(len(nums)):
            if nums[fast] !=0 and nums[slow]==0:
                nums[slow],nums[fast]= nums[fast],nums[slow]
            if nums[slow]!=0:
                slow+=1

solution= Solution()
nums = [0,1,0,3,12]
solution.movezeros(nums)
print(nums)


