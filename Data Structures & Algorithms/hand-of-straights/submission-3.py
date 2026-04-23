from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=defaultdict()
        hand.sort()
        for x in hand:
            count[x]=count.get(x,0)+1
        for num in hand:
            if count[num]==0:
                continue
            for k in range(num,num+groupSize):
                if count.get(k,0)==0:
                    return False
                count[k]-=1
        return True