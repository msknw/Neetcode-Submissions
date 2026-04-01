class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 这个复杂度大概在$O(m^2 n + m n^2)$左右，就如果在resultmap里面能够实现这个O(1)的话就能做到O(n*m)
        result = {}
        
        for word in strs:
            indexes = [0]*26
            for c in word:
                indexes[ord(c) - ord('a')] += 1
            if tuple(indexes) in result:
                result[tuple(indexes)].append(word)
            else:
                result[tuple(indexes)] = [word]
        
        return list(result.values())