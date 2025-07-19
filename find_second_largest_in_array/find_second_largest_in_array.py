from heapq import heappush, heappop

class Solution:
    # def find_second_largest(self, arr:list):
    #     # Code Here
    #     largest = float('-inf')
    #     second_largest = float('-inf')
    #
    #     for num in arr:
    #         if num > largest:
    #             second_largest = largest
    #             largest = num
    #
    #         if second_largest < num < largest:
    #             second_largest = num
    #
    #     if second_largest == float('-inf'):
    #         return -1
    #     else:
    #         return second_largest

    def find_second_largest(self,arr: list):
        if len(arr)<2:
            return None
        heap = []
        for i in arr:
            heappush(heap, i)

            if len(heap)>2:
                heappop(heap)
        return heap[0]


input_arr = [12, 35, 1, 10, 34, 1]
obj= Solution()
print(obj.find_second_largest(input_arr))