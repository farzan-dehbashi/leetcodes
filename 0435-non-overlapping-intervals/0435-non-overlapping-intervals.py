class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        r, e = 0, intervals[0][1]
        for start, end in intervals[1:]:
            if start < e:
                r += 1
                e = min(e, end)
            else:
                e = end
        return r
