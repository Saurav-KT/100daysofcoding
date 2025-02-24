# Problem: find a pair in an array that sums up to a given target
# scenario to test
# 1. Input array can't be empty
# 2. Pair doesnot exist in array
# 3. single element in input array can't form a pair


class FindPair:

  # approach-1: using a brute-force approach to return multiple pair in an array that sums up to a given target
  # @staticmethod
  # def find_pair(arr: list,n:int):
  #     if not arr or len(arr)==1:
  #         raise ValueError("Input array can't be empty or single element in input array can't form a pair")
  #     output=[]
  #     for i in range(len(arr)):
  #         for j in range(i+1, len(arr)):
  #             if (arr[i]+arr[j])==n:
  #                 output.append([arr[i],arr[j]])
  #
  #     if output:
  #         return output
  #     else:
  #        raise ValueError("No pair found")




   # approach-2: using a hash set for optimal performance O(n) time complexity


    @staticmethod
    def find_pair(arr: list, n: int):
        if not arr:
            raise ValueError("Input array can't be empty")
        seen = []
        for num in arr:
            complement = n - num
            if complement in seen:
                return complement,num
            seen.append(num)
        return False


input_arr=[3,5,5,8,2,16]
target=10
print((FindPair.find_pair(input_arr,target)))

