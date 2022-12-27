# Reverse a number

# Method-1
# num=28654
# num=str(num)[::-1]
# print(num)

# Method-2
def reverse_num(number: int) -> int:
    reverse = 0
    while number > 0:
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
    return reverse


num = 28654
print(reverse_num(num))
