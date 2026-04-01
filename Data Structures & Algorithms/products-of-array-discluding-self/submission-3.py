class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum/product by reusing the result array
        # 相当于直接把运算结果放到result里，一轮prefix一轮suffix
        # Time complexity: O(n); Space complexity: O(1)
        n = len(nums)
        
        result = [0] * n

        prefix = 1
        suffix = 1

        for i in range(0, n):
            # 先加
            result[i] = prefix
            prefix *= nums[i]

        for j in range(n-1, -1, -1):
            # 相当于原来的prefix[i]*suffix[i]
            result[j] *= suffix
            suffix *= nums[j]

        return result

        