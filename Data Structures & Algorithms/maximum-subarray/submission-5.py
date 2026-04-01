class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        sumnum = [0] * n
        sumnum[0] = nums[0]
        res = nums[0]
        min_prefix = min(0, nums[0])

        for i in range(1, n):
            sumnum[i] = sumnum[i-1] + nums[i]
            res = max(res, sumnum[i] - min_prefix)
            min_prefix = min(min_prefix, sumnum[i])

        return res            
        
        
