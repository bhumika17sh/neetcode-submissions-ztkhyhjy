import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            
            if hours <= h:
                res = k
                r = k - 1   # try smaller speed
            else:
                l = k + 1   # need faster speed
        
        return res