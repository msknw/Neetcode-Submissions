class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T:O(logn)；二分，但判断区间是否有序
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
                # 这里用 <= 是为了当还有两个数字的时候也能够保持统一
                # [l,c]区间正常
                l = mid + 1
            else:
                r = mid - 1

        return res
 