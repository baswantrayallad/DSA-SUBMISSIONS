class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        total=0
        for i in range(len(nums)):
            num=nums[i] **2
            nums[i]=num
        nums.sort()
        return nums

