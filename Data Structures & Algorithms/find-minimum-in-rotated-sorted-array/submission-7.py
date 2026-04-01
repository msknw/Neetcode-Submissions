class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T:O(logn)；标准的二分法
        res = nums[0]
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (r + l) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                # [l,c]区间正常
                l = mid + 1
            else:
                r = mid - 1

        return res
 