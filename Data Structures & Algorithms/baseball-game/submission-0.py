class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for char in operations:
            if char not in ['+', 'D', 'C']:
                stack.append(int(char))
            elif char=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a+b)
            elif char=='D':
                c=stack.pop()
                stack.append(c)
                stack.append(2*c)
            else:
                stack.pop()
        return sum(stack)