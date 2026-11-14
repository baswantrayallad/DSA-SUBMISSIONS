class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)

        freq=[0]*(n*n+1)

        for row in grid:
            for num in row:
                freq[num]+=1
        
        repeating=-1
        missing=-1

        for num in range(1,n*n+1):
            if freq[num]==2:
                repeating=num
            elif freq[num] ==0:
                missing=num
        return[repeating, missing]