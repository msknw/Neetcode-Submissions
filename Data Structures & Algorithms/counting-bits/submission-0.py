class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def hammingWeight(n: int) -> int:
            cnt = 0
            while n > 0:
                if n & 1 == 1:
                    cnt += 1
                n = n >> 1
            
            return cnt
        
        return [hammingWeight(i) for i in range(n+1)]