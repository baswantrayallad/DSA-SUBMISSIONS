
class Solution:
    def minimumLength(self, s: str) -> int:
        freq=[0]*26

        for ch in s:
            freq[ord(ch) - ord('a')] +=1
        
        ans=0
        for count in freq:
            if count > 0:
                if count % 2 == 1:
                    ans+=1
                else:
                    ans+=2
        return ans
