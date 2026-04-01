class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # T:o(n), S:O(1), Kadane's Algorithm
        n = len(nums)
        curMin, curMax = 1, 1
        res = max(nums)

        for i in range(n):
            if nums[i] == 0:
                curMin, curMax = 1, 1
                continue
            tmp = nums[i] * curMin
            curMin = min(tmp, nums[i] * curMax, nums[i])
            curMax = max(tmp, nums[i] * curMax, nums[i])
            res = max(res, curMax)

        return res