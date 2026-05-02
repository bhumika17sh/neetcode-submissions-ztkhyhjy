class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        cur=1
        if n<0:
            x=1/x
            n=-n
        for _ in range(n):
            cur*=x
        return cur
