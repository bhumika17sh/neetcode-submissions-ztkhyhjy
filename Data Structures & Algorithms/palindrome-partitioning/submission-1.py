class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def is_palindrome(sub):
            return sub==sub[::-1]
        def backtrack(start,path):
            if start==len(s):
                ans.append(path.copy())
                return
            for i in range(start+1,len(s)+1):
                sub=s[start:i]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(i,path)
                    path.pop()
        backtrack(0,[])
        return ans
