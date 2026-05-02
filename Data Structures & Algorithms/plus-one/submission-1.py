class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # ans="".join (str(x) for x in digits)
        # ans1=int(ans)+1
        # return [int(x) for x in str(ans1)]

        if not digits:
            return [1]
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        else:
            return self.plusOne(digits[:-1])+[0]