"""Boyer-Moore Majority Voting Algorithm for Searching elements having more
than ⌊n / 3⌋ times"""

def majority_element(lst):
    cnt1,cnt2=0,0

    el1=None
    el2= None
    for i in range(len(lst)):
        if cnt1==0 and lst[i]!= el2:
            cnt1=1
            el1= lst[i]
        elif cnt2==0 and lst[i]!= el1:
            cnt2=1
            el2= lst[i]
        elif el1== lst[i]:
            cnt1+=1
        elif el2== lst[i]:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1

    cnt1,cnt2=0,0
    output=[]
    n=len(lst)//3 +1
    for i in arr:
        if i==el1:
            cnt1+=1
        elif i== el2:
            cnt2+=1
    if cnt1>= n:
        output.append(el1)
    if cnt2 >= n:
        output.append(el2)
    return sorted(output)


arr=[2,1,1,3,1,4,5,6,3,3,3]
print(majority_element(arr))


