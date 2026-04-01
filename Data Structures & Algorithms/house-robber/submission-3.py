class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        one, two = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            tmp = two
            two = max(nums[i]+one, two)
            one = tmp
        
        print(one, two)
        return max(one,two)