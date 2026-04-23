class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # n=len(senate)
        # rights=[True]*len(senate)
        # rc=senate.count('R')
        # dc=senate.count('D')
        # i=0
        # while rc>0 and dc>0:
        #     if rights[i]:
        #         if senate[i]=='R':
        #             j=(i+1)%n
        #             while senate[j]=='R' or rights[j]==False:
        #                 j=(j+1)%n
        #             rights[j]=False
        #             dc-=1
        #         else:
        #             j=(i+1)%n
        #             while senate[j]=='D' or rights[j]==False:
        #                 j=(j+1)%n
        #             rights[j]=False
        #             rc-=1
        #     i=(i+1)%n
        # return "Radiant" if rc>0 else "Dire"
        r=deque()
        d=deque()
        n=len(senate)
        for i,ch in enumerate(senate):
            if ch=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            ri=r.popleft()
            di=d.popleft()
            if ri<di:
                r.append(ri+n)
            else:
                d.append(di+n)
        return "Radiant" if r else "Dire"