class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand=None
        count=0
        for num in nums:
            if cand==None:
                cand=num
                count+=1
            elif cand == num:
                count+=1
            else:
                count-=1
            
            if count==0:
                cand=num
                count+=1
        return cand