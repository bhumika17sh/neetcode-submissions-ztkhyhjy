class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canship(cap):
            day = 1
            cur = 0

            for w in weights:
                if cur + w > cap:
                    day += 1
                    cur = 0
                cur += w

            return day <= days

        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if canship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left