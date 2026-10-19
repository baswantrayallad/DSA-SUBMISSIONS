class Solution:
    def solve(self,i,j,triangle,dp):
        if i == len(triangle)-1:
            return triangle[i][j]
        if dp[i][j] is not None:
            return dp[i][j]
        down=triangle[i][j]+self.solve(i+1,j,triangle,dp)
        diagnol=triangle[i][j]+self.solve(i+1,j+1,triangle,dp)
        dp[i][j]=min(down,diagnol)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[None]*n for _ in range(n)]
        return self.solve(0,0,triangle,dp)