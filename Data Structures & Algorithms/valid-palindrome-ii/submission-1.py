class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return is_palindrome(l+1,r) or is_palindrome(l,r-1)
            l+=1
            r-=1
        return True
        
        
        # ans={}
        # for char in s:
        #     if char in ans:
        #         ans[s]=ans.get(s,0)-1
        #     ans[s]=ans.get(s,0)+1
