# Given the number n (n >=0),find its factorial.
# Factorial of n is defined as 1 x 2 x … x n. For n = 0, factorial is 1
class Solution:
    def factorial(self,n: int)-> int:
        if n < 0:
            raise ValueError("input value must be greater than equal to zero")
        fact=1
        for i in range(1,n+1):
            fact= fact* i
        return fact

    def factorial_using_recursion(self, n:int):
        if n==0 or n==1:
            return n
        else:
            n= n * self.factorial_using_recursion(n-1)
        return n


solution= Solution()
print(solution.factorial_using_recursion(6))
