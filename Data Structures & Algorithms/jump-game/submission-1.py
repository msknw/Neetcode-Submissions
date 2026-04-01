class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(n)
        # greedy，虽然我也想到了但是想的有点复杂所以没考虑清楚
        # 从后往前如果reachable那么就update一下
        n = len(nums)
        end = n - 1

        for i in range(n-2, -1, -1):
            if nums[i] >= (end - i):
                # reachable
                end = i
        
        return (end == 0)