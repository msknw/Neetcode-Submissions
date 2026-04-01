class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 这个复杂度大概在$O(m*n)$左右
        result = defaultdict(list)
        
        for word in strs:
            indexes = [0]*26
            for c in word:
                indexes[ord(c) - ord('a')] += 1
            
            result[tuple(indexes)].append(word)
        
        return list(result.values())