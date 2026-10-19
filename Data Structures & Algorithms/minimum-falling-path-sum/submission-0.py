class Solution:
    def solve(self,i,j,r,c,matrix,dp):
        if j<0 or j>c-1:
            return float("inf")
        if i==0:
            return matrix[0][j] 
        if dp[i][j] is not None:
            return dp[i][j]
        left=matrix[i][j]+self.solve(i-1,j-1,r,c,matrix,dp)
        root=matrix[i][j]+self.solve(i-1,j,r,c,matrix,dp)
        right=matrix[i][j]+self.solve(i-1,j+1,r,c,matrix,dp)
        dp[i][j]= min(left,root,right)
        return dp[i][j]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        dp=[[None for _ in range(c)] for _ in range(r)]
        mini=float("inf")
        for j in range(0,c):
            mini=min(mini,self.solve(r-1,j,r,c,matrix,dp))
        return mini
