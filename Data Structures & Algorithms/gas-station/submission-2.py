class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        for start in range(n):
            tank=0
            i=start
            count=0
            while count<n:
                tank+=gas[i]
                if tank<cost[i]:
                    break
                tank=tank-cost[i]
                i=(i+1)%n
                count+=1
            if count==n:
                return start
        return -1

