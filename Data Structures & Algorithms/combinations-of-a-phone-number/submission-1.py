class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        mapping={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []
        def backtrack(start,path):
            if start==len(digits):
                ans.append("".join(path))
                return
            digit=digits[start]
            for ch in mapping[digit]:
                path.append(ch)
                backtrack(start+1,path)
                path.pop()
        backtrack(0,[])
        return ans