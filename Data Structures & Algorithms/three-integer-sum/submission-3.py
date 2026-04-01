class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        综合时间复杂度：平均/理想情况： $O(n^2)$
        最坏情况（大量重复元素）： $O(n^3)$，
        因为在 $O(n^2)$ 的循环内部执行了 $O(n)$ 的集合运算。
        
        综合空间复杂度： $O(n)$
        """
        n = len(nums)

        nums.sort()

        result = []

        numCounts = defaultdict(int)
        for index,num in enumerate(nums):
            numCounts[num] += 1

        for i in range(n):
            num = nums[i]
            numCounts[num] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                # 去重
                continue

            rest = -num
            for j in range(i+1, n):
                cnum = nums[j]
                numCounts[cnum] -= 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    # 去重
                    continue
                
                # 为了这个判定就是把前面的i,j防止重复
                if (numCounts[rest-cnum] > 0):
                    result.append([num, cnum, rest-cnum])

            for j in range(i+1 ,n):
                numCounts[nums[j]] += 1

        return result
