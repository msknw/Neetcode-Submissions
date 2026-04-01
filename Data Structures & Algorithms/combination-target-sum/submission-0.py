class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, i, path):
            if cur == target:
                res.append(path[:])
                return
            
            if i >= len(nums) or cur > target:
                return
            
            num = nums[i]
            path.append(num)
            dfs(cur+num, i, path)

            path.pop()
            dfs(cur, i+1, path)
        
        dfs(0, 0, [])
        return res