"""Given an integer array arr[] of size n elements and a positive integer K, the task is to return
the Kth largest element in the given array(not the Kth distinct)
"""

from heapq import heappush, heappop

class LargestElementFinder:
    def find_kth_largest(self, nums: list[str], k: int) -> str:
        heap = []
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)

        return heap[0]

    # def findKthLargest(self, nums: list[int], k: int) -> int:
    #     heap = []
    #     for i in range(len(nums)):
    #         if len(heap)<k:
    #             heappush(heap, nums[i])
    #         else:
    #             if heap[0]< nums[i]:
    #                 heappop(heap)
    #                 heappush(heap, nums[i])
    #     print(heap)
    #
    #     return heap[0]


nums=["1","2","2"]
kth=2
obj=LargestElementFinder()
print(obj.find_kth_largest(nums,kth))


