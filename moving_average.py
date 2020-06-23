from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.size = size
        self.sum = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float

        """
        if not val and len(self.q) == 0:
            return 0.0

        if len(self.q) >= 0 and len(self.q) < self.size:
            self.q.append(val)
            self.sum += val

            return self.sum / len(self.q)


        elif len(self.q) == self.size:
            ele = self.q.popleft()
            print ele
            self.sum -= ele
            self.sum += val
            print self.sum
            return self.sum / self.size


mv = MovingAverage(3)
print mv.next(1)
print mv.next(10)
print mv.next(3)
print mv.next(5)