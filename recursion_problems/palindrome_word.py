def check_palindrome(s: str,i: int,n: int)->bool:
    if i>= len(s)//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return check_palindrome(s,i+1,n)

# check is given string is palindrome without recursion
# def check_palindrome(s:str)->bool:
#     left=0
#     right= len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         else:
#             left+=1
#             right-=1
#     return True

# def check_palindrome(s: str, left: int, right: int):
#     if left>= right:
#         return True
#     if s[left]!= s[right]:
#         return False
#     return check_palindrome(s,left+1, right-1)

# input_st="madam"
# print(check_palindrome(input_st, 0, len(input_st)-1))




input_str="madam"
print(check_palindrome(input_str,0,len(input_str)))