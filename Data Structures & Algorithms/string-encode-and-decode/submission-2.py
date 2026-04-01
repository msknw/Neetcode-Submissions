class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#str6#sss，这种蛮有意思的
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        tmps = ""
        i = 0
        while (i < len(s)):
            if s[i] != '#':
                tmps += s[i]
                i += 1
            else:
                length = int(tmps)
                res.append(s[i+1:i+1+length])
                
                tmps = ""
                i += length + 1

        return res