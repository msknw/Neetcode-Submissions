class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        indexes = {value:index for index,value in enumerate(nums)}
        for i in range(len(nums)):
            num = nums[i]
            another_num = target - num
            if (another_num in indexes):
                if indexes.get(another_num) != i:
                    #finished
                    result.append(i)
                    result.append(indexes.get(another_num))
                
                    return result
            