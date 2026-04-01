class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sdict = {c:s.count(c) for c in s}
            tdict = {c:t.count(c) for c in t}

            return sdict == tdict