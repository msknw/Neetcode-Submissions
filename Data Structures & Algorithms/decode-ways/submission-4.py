class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        # 需要注意这个dp或者memo或者dfs表达的都是什么意思，有时候不一定从0开始处理，两边都可以，怎么方便怎么来
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            # 也可以写成 "10" <= s[i:i+2] <= "26"
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                dp[i] += dp[i+2]
            
        return dp[0]