# fibonacci series of a given number using recursion
# Approach-1
def fibonacci_number(n):
    if n ==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci_number(n-1)+fibonacci_number(n-2)

nterms = int(input("How many terms? "))
for i in range(nterms):
    print(fibonacci_number(i))

# Approach-2
def fibonacci_number(number):
    lst=[0,1]
    for item in range(2,number):
      lst.append(lst[-1]+lst[-2])
    return lst
n=100
print(fibonacci_number(n))

# Approach-3 fibonacci series of a given number without recursion
# n = int(input("enter positive number "))
# prev,next=0,1
# count=0
# if n <= 0:
#     print("enter positive integer")
# else:
#     print(prev,next, end=" ")
#     while count < n:
#             newval= prev+next
#             prev= next
#             next= newval
#             count+=1
#             print(newval, end=" ")

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
