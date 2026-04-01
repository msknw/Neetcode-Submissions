class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort 桶排序，还挺有意思的
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        # 统计完了之后用bucket sort
        buckets = [[] for i in range(len(nums)+1) ]
        for num, cnt in counts.items():
            buckets[cnt].append(num)
        
        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                # 如果有就有没有就会跳过
                result.append(num)
                if len(result) == k:
                    return result