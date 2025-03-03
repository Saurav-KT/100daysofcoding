# count occurrences in a list and store in dictionary key value pair manner

lst=['B','B','A','B','C','A','B',
               'B','A','C']
# expected output={'B': 5, 'A': 3, 'C': 2}

# output={}
# Approach-1 Brute Force Approach O(N^2)
# for i in lst:
#     count=0
#     for j in lst:
#         if i==j:
#             count+=1
#     output[i]= count
#
# print(output)

# Approach-2
output={}
for i in lst:
    if i in output:
        output[i]= output[i]+1
    else:
        output[i]=1
print(output)




