
def reverse_array(input_arr: list):
    if len(input_arr)<=1:
        return

    temp= input_arr.pop()
    reverse_array(input_arr)
    insert_at_bottom(input_arr, temp)

def insert_at_bottom(arr: list, temp):
    if len(arr)==0:
        arr.append(temp)
        return
    val = arr.pop()

    insert_at_bottom(arr, temp)
    arr.append(val)

inputArr=[20,36,19, 46]
reverse_array(inputArr)
print(inputArr)