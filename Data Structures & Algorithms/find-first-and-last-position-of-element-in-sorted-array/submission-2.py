class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = [n, -1]

        # find right
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                # ==
                res[-1] = max(res[-1], mid)
                l = mid + 1

        # find left
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                # ==
                res[0] = min(res[-1], mid)
                r = mid

        return res if res[-1] != -1 else [-1, -1]


