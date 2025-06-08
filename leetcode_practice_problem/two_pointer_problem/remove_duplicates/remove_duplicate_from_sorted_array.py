class RemoveDuplicates:
    def remove_duplicate(self,lst:list)->int:
        slow=0
        for fast in range(1,len(lst)):
            if lst[slow]!=lst[fast]:
                slow+=1
                lst[slow]= lst[fast]
        return slow+1

obj= RemoveDuplicates()
lst=[2,2,4,4,54,56,76,80]
print(obj.remove_duplicate(lst))