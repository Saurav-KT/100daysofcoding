"""Problem
You are provided an array A of size N that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10.

Note: View the sample explanation section for more clarification.

Input format

First line: A single integer  denoting the size of array
Second line:  space-separated integers.

Output format

If the number is divisible by 10, then print Yes. Otherwise, print No."""

# Approach- 1
arr = [12, 4, 80, 3, 19, 7, 20]
# if arr[-1] % 10 == 0:
#     print("yes")
# else:
#     print("No")

# Approach- 2
n = len(arr)


def isDivisible(arr, n):
    lastDigit = int(arr[n - 1]) % 10
    if lastDigit == 0:
        return True

    return False


if isDivisible(arr, n):
    print("Yes")
else:
    print("No")
