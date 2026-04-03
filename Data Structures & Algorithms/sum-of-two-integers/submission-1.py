class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAXINT = 0x7FFFFFFF

        res = (a ^ b) & MASK
        succ = ((a&b) << 1)  & MASK
        while succ != 0:
            tmp = (res ^ succ) & MASK
            succ = ((res & succ) << 1)  & MASK
            res = tmp
        
        if res > MAXINT:
            return ~(res ^ MASK)
        else:
            return res
            