# Write a program to get the multiplication of
# two input matrices and print the result in output.

# Define two matrix A and B in program
A = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9]]
B = [[3, 2, 4],
     [4, 3, 6],
     [2, 7, 5]]

# Define an empty matrix to store multiplication result
multiResult = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

m1 = len(A)
m1_row_size = len(A[0])
m2 = len(B)
m2_row_size = len(B[0])


def solution(A):
    ans = A[0]
    for i in range(1, len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans


arr = [1, 2, 5, 6, 20]
print(solution(arr))


def fairIndexes(A, B) -> int:
    # GET A PREFIX SUM OF EACH ARRAY
    for i in range(1, len(A)):
        A[i] += A[i - 1]
        B[i] += B[i - 1]

    print(A)
    print(B)

    # TRY EACH INDEX
    fair = 0
    for k in range(1, len(A)):
        left_A, right_A = A[k - 1], A[-1] - A[k - 1]
        left_B, right_B = B[k - 1], B[-1] - B[k - 1]
        fair += int(left_A == right_A == left_B == right_B)


    return fair


a = [0, 4, -1, 0, 3]
b = [0, -2, 5, 0, 3]
# a = [2, -2, -3, 3]
# b = [0, 0, 4, -4]

# a = [4, -1, -0, 3]
# b = [-2, 6, 0, 4]
fairIndexes(a,b)
