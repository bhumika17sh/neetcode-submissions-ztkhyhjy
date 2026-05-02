class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n==0:
        #     return 1
        # cur=1
        # if n<0:
        #     x=1/x
        #     n=-n
        # for _ in range(n):
        #     cur*=x
        # return cur
        def power(x,n):
            if n==0:
                return 1
            half=power(x,n//2)
            if n%2 ==0:
                return half*half
            else:
                return half*half*x
        # if n<0:
        #     x=1/x
        #     n=-n
        return power(x,n) if n>0 else 1/power(x,abs(n))