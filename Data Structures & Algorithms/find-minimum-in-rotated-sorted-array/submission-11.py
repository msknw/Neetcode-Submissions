class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T:O(logn)；区间收缩法，更像是二分的样子
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
 