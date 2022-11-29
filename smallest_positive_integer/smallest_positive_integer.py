# Write a function:
# function solution(A);
# that, given an array A of N integers, returns the smallest positive integer(greater than 0) that does not occur in A.

# For example, given A=[3,6,4,7,8], the function should return 5.
# Given A=[1,2,3], the function should return 4.
# Given A=[-1,-3], the function should return 1.

def minpositive(arr):
    if 1 not in arr:
        print("not in arr")
        return 1
    else:
        maxArr = max(arr)
        c1 = set(range(2, maxArr + 2))
        print("c1", c1)
        c2 = c1 - set(arr)
        print("c2", c2)
        return min(c2)


A = [3, 6, 4, 7, 8]
print(minpositive(A))
