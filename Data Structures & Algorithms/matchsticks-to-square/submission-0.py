class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total%4!=0:
            return False
        side=total//4
        matchsticks.sort(reverse=True)
        if matchsticks[0]>side:
            return False
        sides=[0,0,0,0]
        def backtrack(index):
            if index==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]
            stick=matchsticks[index]
            for i in range(4):
                if sides[i]+stick<=side:
                    sides[i]+=stick
                    if backtrack(index+1):
                        return True
                    sides[i]-=stick
                if sides[i]==0:
                    break
            return False
        return backtrack(0)