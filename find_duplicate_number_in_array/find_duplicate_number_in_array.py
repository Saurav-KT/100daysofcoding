# Approach 1: Sort
# Note: This approach modifies individual elements and does not use constant space, and hence does not
# meet the problem constraints. However, it utilizes a fundamental concept that can help solve similar
# problems.

# Intuition
"""In an unsorted array, duplicate elements may be scattered across the array. 
However, in a sorted array, duplicate numbers will be next to each other."""

""" Algorithm
Sort the input array (numsnums).
Iterate through the array, comparing the current number to the previous number (i.e. compare nums[i]nums[i] to nums[i - 1]nums[i−1] where i > 0i>0).
Return the first number that is equal to its predecessor.
"""

# def findDuplicate(nums: list[int]) -> int:
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             return nums[i]

"""Approach 2: Set
Note: This approach does not use constant space, and hence does not meet the problem constraints. However, 
it utilizes a fundamental concept that can help solve similar problems."""

# Intuition

"""As we traverse the array, we need a way to "remember" values that we've seen. If we come across 
a number that we've seen before, we've found the duplicate. An efficient way to record the seen 
values is by adding each number to a set as we iterate over the numsnums array."""

"""Algorithm

In order to achieve linear time complexity, we need to be able to insert elements into a data structure and look them up in constant time. A HashSet/unordered_set is well suited for this purpose. Initialize an empty hashset, seenseen.

Iterate over the array and first check if the current element exists in the hashset (seenseen).

If it does exist in the hashset, that number is the duplicate and can be returned right away.
Otherwise, insert the current element into seenseen, move to the next element in the array and repeat step 2."""

def findDuplicate(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


num = [1, 3, 4, 2, 2]
print(findDuplicate(num))

# def find_duplicate(nums: list[int]) -> int:
#     for element in nums:
#         if element not in new_lst:
#             new_lst.append(element)
#     val = 0
#     for distinct_val in new_lst:
#         if nums.count(distinct_val) > 1:
#             val = distinct_val
#             break
#     return val
