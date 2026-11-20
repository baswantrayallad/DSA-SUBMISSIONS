class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={'a':0, 'b':0, 'c':0}

        left=0
        result=0

        for i in range(len(s)):
            count[s[i]] +=1

            while all(count[ch]>0 for ch in 'abc'):
                count[s[left]]-=1
                left+=1
            result+=left
        return result
