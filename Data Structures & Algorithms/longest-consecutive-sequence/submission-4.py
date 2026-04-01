class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time:O(n); Space: O(n)
        # 但有点太长了
        # boundary
        if not nums:
            return 0

        nset = set(nums)
        visited = set()

        result = 1
        
        for num in list(nset):
            tmpresult = 1
            if num in visited:
                continue
            
            i = 1
            while True:
                # forward
                if ((num + i) in nset) and ((num+i) not in visited):
                    tmpresult += 1
                    # update result
                    result = tmpresult if tmpresult > result else result

                    visited.add(num+i)
                    i += 1
                if (num + i) not in nset:
                    break
            i = -1
            while True:
                #backward
                if ((num + i) in nset) and ((num+i) not in visited):
                    tmpresult += 1
                    # update result
                    result = tmpresult if tmpresult > result else result

                    visited.add(num+i)
                    i -= 1
                if (num + i) not in nset:
                    break
        
        return result