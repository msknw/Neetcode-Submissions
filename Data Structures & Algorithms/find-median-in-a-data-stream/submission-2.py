class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)

    def findMedian(self) -> float:
        self.lst.sort()

        if len(self.lst) == 1:
            return self.lst[0]
        elif len(self.lst) == 2:
            return (self.lst[0]+self.lst[1]) / 2

        if len(self.lst) // 2 == len(self.lst) /2:
            # even
            i = len(self.lst) // 2
            return (self.lst[i-1] + self.lst[i]) / 2
        else:
            # odd
            i = len(self.lst) // 2
            return self.lst[i]

        