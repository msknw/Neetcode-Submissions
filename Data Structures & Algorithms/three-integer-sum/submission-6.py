class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^2)
        Space: O(1) or O(n) extra space depending on the sorting algorithm.
        O(m) for output
        """
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n):
            num = nums[i]
            
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                # 排除重复的
                continue

            l,r = i+1, n-1
            while l < r:
                # 排除重复的
                # while l > i +1 and nums[l] == nums[l-1]:
                #     l += 1
                # while r < n-1 and nums[r] == nums[r+1]:
                #     r -= 1

                tsum = num + nums[l] + nums[r]
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return result
