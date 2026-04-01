class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sorteds = ''.join(sorted(word))
            result[sorteds].append(word)

        return list(result.values())