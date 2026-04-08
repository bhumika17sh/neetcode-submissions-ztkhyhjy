class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        for ch in tokens:
            if ch not in "+-*/":
                self.stack.append(int(ch))
            else:
                b=int(self.stack.pop())
                a=int(self.stack.pop())
                if ch=='+':
                    c= a+b
                elif ch=='-':
                    c= a-b
                elif ch=='*':
                    c= a*b
                elif ch=='/':
                    c= int(a/b)
                self.stack.append(c)
        return self.stack[-1]