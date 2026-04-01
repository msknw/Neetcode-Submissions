class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a, b]，左开右闭
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1