class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.stack=[]
        result=[0] * len(temperatures)
        for i in range(len(temperatures)):
            while self.stack and temperatures[i] > temperatures[self.stack[-1]]:
                j = self.stack.pop()
                result[j] = i - j
            self.stack.append(i)
        return result
