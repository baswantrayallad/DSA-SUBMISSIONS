class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<right:
            mid=(left+right)//2

            required_days=1
            current_load=0

            for weight in weights:
                if current_load+weight>mid:
                    required_days+=1
                    current_load=0
                current_load+=weight
            
            if required_days>days:
                left=mid+1
            else:
                right=mid
        return left