# Given an array of integers. All numbers occur twice except one number which occurs once.
# Find the number in O(n) time & constant extra space.

arr = [3, 5, 4, 5,2, 3, 4]


# This solution works in O(n) time but requires extra space.
#
# The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts.
#
#  XOR of a number with itself is 0.
# XOR of a number with 0 is number itself.

def findSingle(ar, n):
    res = ar[0]
    # Do XOR of all elements and return
    for i in range(1, n):
        res = res ^ ar[i]

    return res


size = len(arr)
print(findSingle(arr, size))
