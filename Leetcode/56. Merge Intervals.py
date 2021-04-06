class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                res += [start, end],
                start = i[0]
                end = i[1]
        res += [start, end],
        return res
