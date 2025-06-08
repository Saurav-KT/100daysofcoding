from heapq import heappop, heappush
class SmallestElementFinder:
    def find_kth_smallest(self, nums: list[int], k: int) -> int:
        minimum_heap=[]

        for num in nums:
            heappush(minimum_heap, -num)
            if len(minimum_heap)> k:
                heappop(minimum_heap)
        print(minimum_heap)
        return -minimum_heap[0]

nums=[3,2,1,5,6,4]
obj= SmallestElementFinder()
print(obj.find_kth_smallest(nums,3))



