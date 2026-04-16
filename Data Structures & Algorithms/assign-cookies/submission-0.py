class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        left=0
        right=0
        count=0
        while left<n and right<m:
            if s[right]>=g[left]:
                count +=1
                left+=1
            right +=1
        return count 