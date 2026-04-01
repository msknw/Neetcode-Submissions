class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, res):
            if n <= 2:
                return n
            
            i = 3
            while i <= n:
                tmp = res[1]
                res[1] = res[0]+res[1]
                res[0] = tmp
                i += 1
            
            return res[1]
        
        return dp(n, [1,2])