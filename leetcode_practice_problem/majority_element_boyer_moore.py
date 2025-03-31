"""Boyer-Moore Majority Voting Algorithm for Searching elements having more
than K Occurrences"""


def majority_element(arr: list)->int:
    cnt=0
    el=None
    n = len(arr)
    for i in range(n):
        if cnt ==0:
            cnt=1
            el=arr[i]
        elif arr[i]==el:
            cnt+=1
        else:
            cnt-=1
    cnt1=0
    for i in range(n):
        if arr[i]== el:
            cnt1+=1
    if cnt1> (len(arr)/2):
        return el
    return -1

lst=[2,2,1,1]
print(majority_element(lst))