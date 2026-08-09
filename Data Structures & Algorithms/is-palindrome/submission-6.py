class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c.lower() for c in s if c.isalnum())
        return str(s)==str(s)[::-1]