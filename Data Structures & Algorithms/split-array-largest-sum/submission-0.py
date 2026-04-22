class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(cap):
            parts = 1
            cur = 0

            for w in nums:
                if cur + w > cap:
                    parts += 1
                    cur = 0
                cur += w

            return parts <= k

        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if split(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left