"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

# Approach-1 Hashmap technique
# def majority_element(nums: list[int]) -> int:
#     my_dict = {}
#     for i in nums:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#
#     keymax = max(zip(my_dict.values(), my_dict.keys()))[1]
#     return keymax
#
# print(majority_element([3,2,3]))

