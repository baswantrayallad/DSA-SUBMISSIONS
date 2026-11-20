class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n,m=len(s),len(p)

        if m>n:
            return []

        result=[]
        count=[0]*26

        for ch in p:
            count[ord(ch)-ord('a')]+=1
        
        for i in range(m):
            count[ord(s[i])-ord('a')]-=1
        
        if all(x==0 for x in count):
            result.append(0)

        for i in range(m,n):
            count[ord(s[i])-ord('a')] -=1
            count[ord(s[i-m])-ord('a')] +=1
            if all(x==0 for x in count):
                result.append(i-m+1)
        return result

        
