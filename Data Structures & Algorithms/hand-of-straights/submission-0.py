from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for num in sorted(hand):
            if count[num] > 0:
                # try to form a group
                for i in range(groupSize):
                    if count[num + i] == 0:
                        return False
                    count[num + i] -= 1
        
        return True