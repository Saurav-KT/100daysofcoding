class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = float('-inf')
        second_largest = float('-inf')

        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num

            if second_largest < num < largest:
                second_largest = num

        if second_largest == float('-inf'):
            return -1
        else:
            return second_largest

arr = [12, 35, 1, 10, 34, 1]
obj= Solution()
print(obj.getSecondLargest(arr))