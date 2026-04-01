class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sweep line search，挺有意思的
        event = []
        for l, r in intervals:
            event.append((l, -1))
            event.append((r, 1))
        
        # event.sort(key = lambda x:x[0])
        event.sort(key=lambda x:(x[0], x[1]))

        res = []
        start_time = 0
        cnt = 0

        print(event)

        for pos, ptype in event:
            if cnt == 0:
                start_time = pos
            
            cnt -= ptype

            if cnt == 0:
                res.append([start_time, pos])

        return res