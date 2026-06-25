class Solution:
    def trap(self, height: List[int]) -> int:
        lwall=0
        rwall=0
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        for i in range(n):
            j=-i-1
            maxleft[i]=lwall
            maxright[j]=rwall
            lwall=max(lwall,height[i])
            rwall=max(rwall,height[j])
        summ=0
        for i in range(n):
            pot=min(maxleft[i],maxright[i])
            summ+=max(0,pot-height[i])
        return summ