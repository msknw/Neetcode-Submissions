class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(n^2)
        # dp，注意这里的dp[i]可以用bool来表示，单纯起一个辨别作用，没有太多的其他作用
        # mark 这个dp[i]是不是能够可达
        n = len(nums)
        dp = [False] * n

        dp[-1] = True
        end = n-1

        for i in range(n-2, -1, -1):
            end = min(n, i+nums[i])
            for j in range(i+1, end+1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]