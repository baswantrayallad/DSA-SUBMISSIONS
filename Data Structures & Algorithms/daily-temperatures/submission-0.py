class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n

        for i in range(0,n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pre_day=stack.pop()
                result[pre_day]=i-pre_day
            stack.append(i)
        return result