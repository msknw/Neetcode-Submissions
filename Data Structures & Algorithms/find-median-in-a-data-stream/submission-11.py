import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 先加到这个large当中
        heapq.heappush(self.large, num)
        
        while self.small and self.large and -self.small[0] > self.large[0]:
            poped = -heapq.heappop(self.small)
            heapq.heappush(self.large, poped)
            
        while len(self.large) - len(self.small) > 1:
            poped = heapq.heappop(self.large)
            heapq.heappush(self.small, -poped)
        while len(self.small) - len(self.large) > 1:
            poped = -heapq.heappop(self.small)
            heapq.heappush(self.large, poped)

    def findMedian(self) -> float:
        print(self.small, self.large)
        # 相等
        if len(self.large) == len(self.small):
            return (self.large[0]+(-self.small[0])) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]    
        
        