class Solution:
    def dfs(self,r,c,visited,rows,cols,board):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if visited[r][c]==1:
            return
        if board[r][c]=='X':
            return
        visited[r][c]= 1
        self.dfs(r-1,c,visited,rows,cols,board)
        self.dfs(r,c-1,visited,rows,cols,board)
        self.dfs(r,c+1,visited,rows,cols,board)
        self.dfs(r+1,c,visited,rows,cols,board)






    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]

        r=0
        c=cols-1
        for c in range(cols):
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,visited,rows,cols,board)

        r=0
        c=0
        for r in range(rows):
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,visited,rows,cols,board)

        r=rows-1
        c=0
        for c in range(cols):
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,visited,rows,cols,board)

        r=0
        c=cols-1
        for r in range(rows):
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c,visited,rows,cols,board)



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and visited[r][c] == 0:
                    board[r][c]='X'
        