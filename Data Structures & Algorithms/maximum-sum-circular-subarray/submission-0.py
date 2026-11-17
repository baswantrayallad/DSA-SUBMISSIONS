class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        curr_max=0
        max_sum=float("-inf")

        curr_min=0
        min_sum=float("inf")

        for num in nums:

            total+=num

            curr_max=max(num,curr_max+num)
            max_sum=max(max_sum,curr_max)

            curr_min=min(num,curr_min+num)
            min_sum=min(min_sum,curr_min)

        if max_sum < 0:
            return max_sum
        
        return max(max_sum,total - min_sum)
