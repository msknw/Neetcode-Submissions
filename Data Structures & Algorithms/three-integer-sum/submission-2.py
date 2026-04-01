class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        综合时间复杂度：平均/理想情况： $O(n^2)$
        最坏情况（大量重复元素）： $O(n^3)$，
        因为在 $O(n^2)$ 的循环内部执行了 $O(n)$ 的集合运算。
        
        综合空间复杂度： $O(n)$
        """
        n = len(nums)

        result = set()
        visited = set()

        numRevDict = defaultdict(set)
        for index,num in enumerate(nums):
            numRevDict[num].add(index)

        for i in range(n):
            num = nums[i]
            if i not in numRevDict[num]:
                continue

            rest = -num
            for j in range(i+1, n):
                cnum = nums[j]
                if j not in numRevDict[cnum]:
                    continue
                
                # visited
                # numRevDict[cnum].remove(j)
                if (numRevDict[rest-cnum] - {i,j}):
                    #randomly
                    # numRevDict[rest-cnum].pop()
                    result.add(tuple(sorted([num, cnum, rest-cnum])))
            
            # visited
            numRevDict[num].remove(i)

        return [list(t) for t in result]
