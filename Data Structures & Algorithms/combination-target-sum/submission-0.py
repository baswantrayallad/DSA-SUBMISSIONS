class Solution:
    def solve(self, ind, total, subset,num, target, result):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if ind>=len(num):
            return
        Sum=total+num[ind]
        subset.append(num[ind])
        self.solve(ind, Sum, subset, num, target, result)
        Sum=total
        subset.pop()
        self.solve(ind+1, Sum, subset, num, target, result)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,[],nums,target,result)
        return result
        