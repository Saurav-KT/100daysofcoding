# input:nums = [1, 3, 4, 2, 2]
# Output: 2
# -------------------------------------------------------
# Approach 1: Sort
# Note: This approach modifies individual elements and does not use constant space, and hence does not
# meet the problem constraints. However, it utilizes a fundamental concept that can help solve similar
# problems.

""" Algorithm
Sort the input array (numsnums).
Iterate through the array, comparing the current number to the previous number (i.e. compare nums[i]nums[i] to nums[i - 1]nums[i−1] where i > 0i>0).
Return the first number that is equal to its predecessor.
"""
# ----------------------------------------------------------------
# Approach 2:
# Intuition
"""In an unsorted array, duplicate elements may be scattered across the array.However, in a sorted array, duplicate numbers will be next to each other.
Approach 2: Set
Note: This approach does not use constant space, and hence does not meet the problem constraints. However, 
it utilizes a fundamental concept that can help solve similar problems.
As we traverse the array, we need a way to "remember" values that we've seen. If we come across 
a number that we've seen before, we've found the duplicate. An efficient way to record the seen 
values is by adding each number to a set as we iterate over the numsnums array.
"""

"""Algorithm
In order to achieve linear time complexity, we need to be able to insert elements into a data structure and look them up in constant time. A HashSet/unordered_set is well suited for this purpose. Initialize an empty hashset, seenseen.
Iterate over the array and first check if the current element exists in the hashset (seenseen).
If it does exist in the hashset, that number is the duplicate and can be returned right away.
Otherwise, insert the current element into seen, move to the next element in the array and repeat step 2."""


# Approach-1
def check_duplicate(num: list[int]) -> int:
    num = num.sort()
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            return num[i]
    return -1


# Approach-2
def check_duplicate(num: list[int]) -> int:
    s = set()
    for element in num:
        if element in s:
            return element
        s.add(element)


nums = [1, 3, 4, 2, 8]
print(check_duplicate(nums))
