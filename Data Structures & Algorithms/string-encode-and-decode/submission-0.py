class Solution:

    def encode(self, strs: List[str]) -> str:
        # using ord
        tmps = []
        for s in strs:
            for c in s:
                tmps.append(str(ord(c)))
            tmps.append(str(-1))
        
        return " ".join(tmps)


    def decode(self, s: str) -> List[str]:
        result = []
        tmps = []
        ords = s.split()
        for o in ords:
            co = int(o)
            if co != -1:
                tmps.append(chr(co))
            else:
                result.append("".join(tmps))
                tmps.clear()
        
        return result
