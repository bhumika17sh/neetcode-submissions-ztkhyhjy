class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(path,openc,closec):
            if len(path)==2*n:
                res.append("".join(path))
                return
            if openc < n:
                path.append("(")
                backtrack(path,openc+1,closec)
                path.pop()
            if closec<openc:
                path.append(")")
                backtrack(path,openc,closec+1)
                path.pop()
        backtrack([],0,0)
        return res