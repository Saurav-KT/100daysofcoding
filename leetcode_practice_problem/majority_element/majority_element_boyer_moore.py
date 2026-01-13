"""Boyer-Moore Majority Voting Algorithm for Searching elements having more
than ⌊n / 2⌋ times"""

def majority_element(arr: list)->int:
    count=0
    el=None
    n = len(arr)
    for i in range(n):
        if count ==0:
            count=1
            el=arr[i]
        elif arr[i]==el:
            count+=1
        else:
            count-=1
    cnt1=0
    for i in range(n):
        if arr[i]== el:
            cnt1+=1
    if cnt1> (len(arr)/2):
        return el
    return -1

lst=[1,1, 2, 1, 2,1]
print(majority_element(lst))