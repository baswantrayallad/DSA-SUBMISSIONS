class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix_sum=0
        freq={0:1}

        for num in nums:

            prefix_sum+=num

            count+=freq.get(prefix_sum-goal,0)

            freq[prefix_sum] = freq.get(prefix_sum,0)+1
        
        return count