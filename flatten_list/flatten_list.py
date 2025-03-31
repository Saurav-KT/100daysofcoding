# from pandas.core.common import flatten

# Approach-1
lst = [24, 5, 49, 28, [1, 3, 29, [2, 6, 32, 67]]]


# new_lst=[]
# print(list(flatten(lst)))

# def flatten(test_list):
#     if isinstance(test_list, list):
#         if len(test_list) == 0:
#             return []
#         first, rest = test_list[0], test_list[1:]
#         return flatten(first) + flatten(rest)
#     else:
#         return [test_list]


def flatten(input_lst,output_lst=[]):
    """ Objective : to flatten nested list
        Input parameters : input_lst
        Return value:output_lst
    """
    for element in input_lst:
        if type(element)!=list:
            output_lst.append(element)
        else:
            flatten(element,output_lst)
    return output_lst


x=flatten(lst)
print(x)
