class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 或者计算sum，因为一共就只有一个缺失
        # T:O(n), S:O(1)
        n = len(nums)
        cnt = n
        for i in range(n):
            cnt += i - nums[i]
        
        return cnt