class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 用bisect
        n = len(nums)

        def bs_left(nums, target):
            # 用[a,b]实现
            n = len(nums)
            l, r = 0, n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r =  mid - 1
            
            return l

        def bs_right(nums, target):
            # 用[a,b]实现
            n = len(nums)
            l, r = 0, n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] > target:
                    r = mid - 1
                # elif nums[mid] < target:
                #     l = mid + 1
                else:
                    l = mid + 1
            
            return l

        left = bs_left(nums, target)
        right = bs_right(nums, target)
        print(left, right)
        if left >= n or nums[left] != target:
            return [-1, -1]
        right = bs_right(nums, target)
        return [left, right-1]