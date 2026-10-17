class Solution:

    def solve(self,index,nums,dp):
        if index==0:
            return nums[index]
        if index==-1:
            return 0
        if dp[index] != -1:
            return dp[index]
        pick=nums[index]+self.solve(index-2,nums,dp)
        not_pick=0+self.solve(index-1,nums,dp)
        dp[index] = max(pick,not_pick)
        return dp[index]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        dp=[-1]*(n-1)
        ans1=self.solve(n-2, nums[0:n-1], dp)
        dp=[-1]*(n-1)
        ans2=self.solve(n-2, nums[1:n], dp)
        return max(ans1,ans2)

        
         