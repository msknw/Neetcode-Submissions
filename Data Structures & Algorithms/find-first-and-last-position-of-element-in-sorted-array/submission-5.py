import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 用bisect
        n = len(nums)
        left = bisect.bisect_left(nums, target)
        if left >= n or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)
        return [left, right-1]