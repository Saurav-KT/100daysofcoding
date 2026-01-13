'''Given an array arr[] consisting of n integers, the task is to find all
the array elements which occurs more than floor(n/3) times.
Note: The returned array of majority elements should be sorted.'''

def find_majority(arr,n):
    counter = {}
    output=[]
    frequency = (n//3)
    for i in arr:
        if i in counter:
               counter[i]+= 1
               if counter[i] > frequency:
                   output.append(i)
        else:
            counter[i] = 1

    # for k,v in counter.items():
    #     if v >frequency:
    #         output.append(k)
    return sorted(output)

input_arr = [2, 2, 3, 1, 3, 2, 1, 1]
print(find_majority(input_arr, len(input_arr)))





