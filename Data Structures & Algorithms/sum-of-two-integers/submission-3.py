class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 也可以b做carry然后a做res
        MASK = 0xFFFFFFFF
        MAXINT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        
        if a > MAXINT:
            return ~(a ^ MASK)
        else:
            return a
            