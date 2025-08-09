from heapq import heappush, heappushpop,nlargest
from collections import defaultdict, Counter

# def top_k_frequent(nums: list[int], k: int):
#     list_count= Counter(nums)
#     lst= nlargest(k,list_count.keys(),list_count.get)
#     return lst
def top_k_frequent(nums: list[int], k: int):
    freq = defaultdict(int)
    for n in nums:
        freq[n] += 1
    heap = []
    for key, count in freq.items():
        if len(heap) == k:
            heappushpop(heap, (count, key))
        else:
            heappush(heap, (count, key))
    return [item[1] for item in heap]
#
input_nums = [1,1,1,2,2,3,5,5,9,5]

print(top_k_frequent(input_nums,2))



