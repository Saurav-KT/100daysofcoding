# Given an array A[] of n numbers and another number x,
# the task is to check whether or not there exist two elements in A[] whose sum is exactly x.
# Input arr = [0, -1, 2, -3, 1]
# n=-2
# output= Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2

# Input: arr = [1, -2, 1, 0, 5], x = 0
# Output: No

def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if A[i] + A[j] == x:
                return 1
    return 0


arr = [0, -1, 2, -3, 1]
size = len(arr)
n = 3
if chkPair(arr, size, n):
    print("Yes")
else:
    print("No")

# Two pointer technique to implement the solution