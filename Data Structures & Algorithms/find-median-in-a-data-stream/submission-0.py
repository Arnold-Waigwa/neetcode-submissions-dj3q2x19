class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
       

    def findMedian(self) -> float:
        #if odd
        N = len(self.arr) 
        if N % 2 != 0:
            mid = N // 2
            return self.arr[mid]
        mid = N // 2
        return (self.arr[mid-1] + self.arr[mid]) / 2
        
        