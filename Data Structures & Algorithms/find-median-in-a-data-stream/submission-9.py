import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 或者你就是用判断
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
            
        
        while len(self.large) - len(self.small) > 1:
            poped = heapq.heappop(self.large)
            heapq.heappush(self.small, -poped)
        while len(self.small) - len(self.large) > 1:
            poped = -heapq.heappop(self.small)
            heapq.heappush(self.large, poped)

    def findMedian(self) -> float:
        print(self.small, self.large)
        # 相等
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (self.large[0]+(-self.small[0])) / 2 
        
        