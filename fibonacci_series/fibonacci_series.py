# fibonacci series of a given number using recursion

# Approach-1
# def fibonacci_number(n):
#     if not isinstance(n, int):
#         raise TypeError("n vaiables not of type int ")
#     if int(n) <= 1:
#         return n
#     else:
#         return fibonacci_number(n-1)+fibonacci_number(n-2)
#
# nterms = int(input("How many terms? "))
# for i in range(nterms):
#     print(fibonacci_number(i))

# Approach-2 fibonacci series of a given number without recursion
n = int(input("enter positive number "))
n1, n2 = 0, 1
count = 0
if n <= 0:
    print("enter positive integer")
else:
    while count < n:
        newval = n1 + n2
        n1 = n2
        n2 = newval
        count += 1

# T = int(input("Enter the number of test cases"))
# i = 0
# if 1 <= T <= 10:
#     while i < T:
#         S = input("Enter string")
#         outputChar = ''
#         if 1 <= len(S) <= 30:
#             for eachChar in S:
#                 outputChar = eachChar + outputChar
#             i += 1
#             print(outputChar)
