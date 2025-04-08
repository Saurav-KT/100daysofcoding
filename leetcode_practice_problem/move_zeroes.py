# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
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
    def movezeros(self, nums: list[int])->list:
        slow=0
        for fast in range(len(nums)):
            if nums[fast] !=0 and nums[slow]==0:
                nums[slow],nums[fast]= nums[fast],nums[slow]
            if nums[slow]!=0:
                slow+=1
        return nums

    # solved using two pointer
    def move_zeroes(self, lst_move_zero:list[int])->list:
        non_zero_ptr=0
        # Move all non-zero elements to the front
        for i in range(len(lst_move_zero)):
            if lst_move_zero[i] !=0:
                lst_move_zero[non_zero_ptr]= lst_move_zero[i]
                non_zero_ptr+=1

        # Fill the remaining positions with zeros
        for i in range(non_zero_ptr,len(lst_move_zero)):
            lst_move_zero[i]=0
        return lst_move_zero



solution= Solution()
nums = [0,1,0,3,12]
print(solution.move_zeroes(nums))






