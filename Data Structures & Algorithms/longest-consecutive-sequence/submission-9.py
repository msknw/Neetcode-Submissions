class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time:O(n); Space: O(n)
        # 现在改进一下只考虑从一个方向进行搜寻，那么就需要这个找到seq的起始，怎么找呢；
        # 如果如果num-1在里面的话那我这个其实后面都是会访问到的，不然的话我就是起始点；
        # 这样可以省掉一个visited set
        # boundary
        if not nums:
            return 0

        nset = set(nums)

        result = 1
        
        for num in nset:
            length = 1
            if num - 1 not in nset:
                # 我就是起始
                # 然后如果num - 1 在的话就是跳过当前这个数
                while num + 1 in nset:
                    length += 1
                    num += 1
                # end
                result = max(length, result)

        return result