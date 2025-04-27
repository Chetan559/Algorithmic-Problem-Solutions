class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        intervals.sort()

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if res and end <= res[-1][1]:
                continue

            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(intervals[j][1], end)
                else:
                    break
            
            res.append([start, end])

        return res
        