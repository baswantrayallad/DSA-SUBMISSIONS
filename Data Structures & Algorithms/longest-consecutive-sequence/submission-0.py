class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        last_smaller=float("-inf")
        count=0
        longest=0
        for i in range (len(nums)):
            num=nums[i]
            if num-1 == last_smaller:
                count+=1
                last_smaller=num
            elif num !=last_smaller:
                count=1
                last_smaller=nums[i]
            longest=max(longest, count)
        return longest

        