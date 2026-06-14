class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for u in nums:
            if u in seen:
                return True
            seen.add(u)

        return False