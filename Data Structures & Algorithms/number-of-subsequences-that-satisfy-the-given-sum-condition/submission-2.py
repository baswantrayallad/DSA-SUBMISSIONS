class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        MOD=10**9+7

        nums.sort()

        power=[1]*n

        for i in range(1,n):
            power[i] = (power[i-1]*2) % MOD

        left=0
        right=n-1
        ans=0

        while left<=right:
            if nums[left] + nums[right] <= target:
                ans= (ans+ power[right-left])%MOD
                left+=1
            else:
                right-=1
        return ans