class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 不错，一次就写出了optimal，优化了一下去掉了continue
        # T:O(logn)
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # 看target在不在里面：
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    #不在，那么在另一边
                    l = m+1
            elif nums[m] <= nums[r]:
                # 看target在不在里面：
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    #不在，那么在另一边
                    r = m-1
        
        return -1