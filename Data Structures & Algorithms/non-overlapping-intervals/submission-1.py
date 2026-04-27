class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            intervals.sort(key=lambda x:x[0])
            count=0
            maxx=intervals[0][1]
            n=len(intervals)
            for i in range(1,n):
                if maxx>intervals[i][0]:
                    count+=1
                    maxx=min(maxx,intervals[i][1])
                else:
                    maxx=intervals[i][1]
            return count
