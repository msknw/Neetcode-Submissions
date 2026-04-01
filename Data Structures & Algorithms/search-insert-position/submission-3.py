import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 试一试library
        idx = bisect.bisect_left(nums, target)
        return idx
