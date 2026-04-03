class Solution:
    def countBits(self, n: int) -> List[int]:
        # T:O(n)；有最优子结构，所以是dp
        
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp