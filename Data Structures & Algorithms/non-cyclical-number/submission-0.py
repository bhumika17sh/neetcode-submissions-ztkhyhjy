class Solution:
    def isHappy(self, n: int) -> bool:
        
        ans=set()
        while n!=1:
            if n in ans:
                return False
            ans.add(n)
            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n//=10
            n=total
        return True