class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T:O(logn)；但不太标准
        n = len(nums)
        l,r = 0, n-1
        if nums[l] < nums[r]:
            return nums[l]

        while nums[l] > nums[r] and r-l > 1:
            c = (r+l) // 2
            if nums[l] < nums[c]:
                # [l,c]区间正常
                l = c+1
            else:
                r = c

        return min(nums[l], nums[r])
 