class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        
        for i in range(n-1):
            a,b=b,a+b
        
        if(n == 0):return 0
        return b
        