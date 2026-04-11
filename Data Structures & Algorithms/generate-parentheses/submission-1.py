class Solution:
    def solve(self, ind, total, brackets, result):
        if ind>=len(brackets):
            if total==0:
                result.append("".join(brackets))
            return

        if total>len(brackets)//2:
            return
        if total < 0:
            return
        brackets[ind]="("
        Sum = total+1
        self.solve(ind+1, Sum, brackets, result)
        brackets[ind]=")"
        Sum = total-1
        self.solve(ind+1, Sum, brackets, result)
    def generateParenthesis(self, n: int) -> List[str]:
        brackets=[" "]*(n*2)
        result=[]
        self.solve(0, 0, brackets, result)
        return result