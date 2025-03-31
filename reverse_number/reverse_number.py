# Reverse a number

# Method-1
# num=28654
# num=str(num)[::-1]
# print(num)

# Method-2
def reverse_num(number: int) -> int:
    reverse = 0
    is_negative= number<0
    number= abs(number)
    while number > 0:
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
    return -reverse if is_negative else reverse


num = 21
print(reverse_num(num))
