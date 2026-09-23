class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visted=deepcopy(image)
        rows=len(visted)
        cols=len(visted[0])

        initial_color=visted[sr][sc]
        queue=deque()
        queue.append((sr,sc))

        while len(queue) !=0:
            i,j=queue.popleft()
            visted[i][j]=color
            for x, y in ([-1,0],[1,0],[0,1],[0,-1]):
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if visted[new_i][new_j] != initial_color:
                    continue
                
                queue.append((new_i,new_j))
        return visted

        
        