class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)
        return (len(nset) != len(nums))