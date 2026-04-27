class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        n=len(intervals)
        new=[]
        intervals.sort(key=lambda x:x[0])
        curr=intervals[0]
        for i in range(1,n):
            if curr[1]>=intervals[i][0]:
                curr[1]=max(curr[1],intervals[i][1])
            else:
                new.append(curr)
                curr=intervals[i]
        new.append(curr)
        return new
                