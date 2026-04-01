class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 普通的做法 Time complexity: O(nlogn)；Space complexity: O(n)
        counts = defaultdict(list)
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        result = []
        sortedcounts=sorted(counts.items(), key = lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(sortedcounts[i][0])

        return result