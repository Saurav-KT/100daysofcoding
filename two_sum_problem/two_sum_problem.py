# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3: Input: nums = [3,3], target = 6
# Output: [0,1]

# def two_sum(nums: list[int], target: int) -> list[int]:
#     result = 0
#     return_index = []
#     for element in range(len(nums)):
#         for inner_element in range(element + 1, len(nums)):
#             result = nums[element] + nums[inner_element]
#             if result == target:
#                 return_index.append([element, inner_element])
#     return return_index

#
# nums = [3, 2, 4, 1, 5, 3]
# target = 6
# print(two_sum(nums, target))

def two_sum(nums: list[int], target:int)-> list[int]:
    num_map={} # Create hash map to store number -index pair
    for i, num in enumerate(nums):
        complement= target- num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num]= i
    return []


nums = [3, 2, 4, 1, 5, 3]
target = 6
print(two_sum(nums, target))


