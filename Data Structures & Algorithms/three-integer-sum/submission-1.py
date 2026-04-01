class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
