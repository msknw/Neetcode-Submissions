class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 可以一直异或 
        # T: O(n), S:O(1)
        n = len(nums)
        xoor = n
        for i in range(n):
            xoor = xoor ^ i ^ nums[i]
        
        return xoor