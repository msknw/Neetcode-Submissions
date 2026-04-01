class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a, b)，左闭右开
        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1