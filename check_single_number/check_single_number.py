# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums: list[int]) -> int:
    nums.sort()
    stack = []
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if nums[i] not in stack:
            stack.append(nums[i])
        else:
            stack.pop()
    return stack[0]


arr = [1, 0, 1]
print(singleNumber(arr))
