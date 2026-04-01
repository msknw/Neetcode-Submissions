class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 暴力 O(n^2)
        # 学到了新知识，prefix sum/product
        result = []

        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        total_pre = nums[0]
        total_suf = nums[n-1]
        
        prefix[1] = nums[0]
        suffix[n-2] = nums[n-1]

        for i in range(1, n-1):
            total_pre *= nums[i]
            total_suf *= nums[n-i-1]

            prefix[i+1] = total_pre
            suffix[n-i-1-1] = total_suf

        for i in range(n):
            prod = prefix[i]*suffix[i]
            result.append(prod)

        return result

        