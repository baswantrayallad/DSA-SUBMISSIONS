class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        total=0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                total+=customers[i]
            
        window_sum=0

        for i in range(minutes):
            if grumpy[i] == 1:
                window_sum += customers[i]
        
        max_extra= window_sum

        for i in range(minutes,len(customers)):
            if grumpy[i] == 1:
                window_sum += customers[i]
            
            if grumpy[i-minutes] == 1:
                window_sum -= customers[i-minutes]
            
            max_extra=max(max_extra,window_sum)
        
        return total + max_extra