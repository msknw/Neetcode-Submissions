class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        resultmaps = []
        for word in strs:
            ishave = False
            worddict = {c:word.count(c) for c in word}
            if result:
                for i, groupdict in enumerate(resultmaps):
                    if worddict == groupdict:
                        result[i].append(word)
                        ishave = True
            if not ishave:
                resultmaps.append(worddict)
                result.append([word])
        
        return result