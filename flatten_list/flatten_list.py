from pandas.core.common import flatten

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


def flatten(list1,list2=[]):
    ''' Objective : to flatten a list 1
        Input parameters :list1,list2
        Return value:list2
    '''
    for element in list1:
        if type(element)!=list:
            list2.append(element)
        else:
            flatten(element,list2)

x=flatten(lst)
print(x)
