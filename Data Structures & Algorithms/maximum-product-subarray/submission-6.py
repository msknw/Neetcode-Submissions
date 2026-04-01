class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # T:o(n), S:O(1), 更简洁一些
        n = len(nums)
        prefix = suffix = 0
        res = nums[0]

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-i-1] * (suffix or 1)
            res = max(res, prefix, suffix)
        return res