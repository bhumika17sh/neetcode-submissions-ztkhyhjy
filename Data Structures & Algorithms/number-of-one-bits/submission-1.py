class Solution:
    def hammingWeight(self, n: int) -> int:
        # count=0
        # array=[int(x) for x in bin(n)]
        # for i in array:
        #     if i==1:
        #         count+=1
        # return count

        # return bin(n).count('1')
        count=0
        while n:
            count+= n&1
            n>>=1
        return count
