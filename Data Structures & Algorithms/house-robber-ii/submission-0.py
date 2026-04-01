class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            one, two = 0, 0
            for i in range(len(nums)):
                tmp = two
                two = max(nums[i]+one, two)
                one = tmp
            
            return two
        
        return max(helper(nums[1:]), helper(nums[:-1]))
