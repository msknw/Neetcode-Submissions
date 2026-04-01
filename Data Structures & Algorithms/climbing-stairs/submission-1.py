class Solution:
    def climbStairs(self, n: int) -> int:
        # 都已经两个了写个简单点的吧
        one, two = 1, 1
        for i in range(n-1):
            tmp = two
            two = one + two
            one = tmp

        return two