class Solution:
    # time complexity: O(m + n), space complexity: O(m + n)
    """维度,长度 + # 方案,"ord() + ""-1"" 方案"
空间膨胀,极小。每个单词只多几个字节的元数据。,"极大。一个字母 'a' (1字节) 变成 ""97 "" (3字节)，空间通常膨胀 3-5 倍。"
CPU 开销,很低。主要是切片和数字转换。,较高。每个字符都要调用 ord/chr，且要进行大量的 split 和 int 转换。
字符支持,支持 ASCII 256（乃至全 Unicode）。,支持全 Unicode。"""
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
