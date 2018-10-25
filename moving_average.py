"""
Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.
"""


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.size = size
        self.Que = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.Que.append(val)

        if len(self.Que) > self.size:
            self.sum -= self.Que.popleft()
        return float(self.sum) / float(len(self.Que))


l = [1, 2, 3, 4, 5, 6, 7, 8]

obj = MovingAverage(3)

for i in l:
    print(obj.next(i))











