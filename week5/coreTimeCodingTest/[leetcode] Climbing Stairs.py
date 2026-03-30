class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [None]*(n+1)
        dp[0]=1
        dp[1]=1


        def fib(n):
            if n == 0 or n == 1:
                return 1
            if dp[n] is None:
                dp[n] = fib(n-1) + fib(n-2)
            return dp[n]
                
        return fib(n)
        