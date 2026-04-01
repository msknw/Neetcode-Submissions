class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return n
        elif target == nums[-1]:
            return n-1
        
        # in array
        l, r = 0, n
        while l < r:
            mid = (l + r)  // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        
        return l
