class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [nums[0]]*n
        sufsum = [nums[-1]]*n

        res = nums[0]

        for i in range(n):
            if i > 0:
                tmppre = presum[i-1] if presum[i-1] != 0 else 1
                presum[i] = nums[i] * tmppre
                tmpsuf = sufsum[n-i] if sufsum[n-i] != 0 else 1
                sufsum[n-i-1] = nums[n-i-1] * tmpsuf
        
            res = max(res, nums[i], presum[i], sufsum[n-i-1])
        print(presum, sufsum)
        return res