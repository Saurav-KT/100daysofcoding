# Find the Max Number in an Array


class MaxFinder:

    # Approach-1
    # @staticmethod
    # def find_maximum_number(num:List)->int:
    #
    #     if not num:
    #         raise ValueError("Array cannot be empty")
    #
    #     max_number= num[0]
    #     for item in num:
    #         max_number= max(max_number,item)
    #     return max_number

    # Approach-2
    @staticmethod
    def find_maximum_number(arr:list)->int:
        if not arr:
            raise ValueError("array cannot be empty")
        max_number= arr[0]
        for item in arr:
            if item > max_number:
                max_number= item
        return max_number






input_arr=[4, 2, 1,6,10,45,11]
max_val= MaxFinder.find_maximum_number(input_arr)
print("maximum", max_val)