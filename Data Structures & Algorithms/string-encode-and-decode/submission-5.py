class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#str6#sss，这种蛮有意思的
        """
        Time complexity: O(m).  Space complexity: O(m+n)
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while (i < len(s)):
            ## == 改进 用while ===
            j = i
            while (s[j] != '#'):
                # === 再改进 用临时指针j寻找分隔符 ===
                """
                s[i:j] 是由 C 语言底层实现的，这比你在循环里用 tmps += s[i] 一个个字符拼接要快得多。
                """
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            
            i = j + length + 1

        return res