class Solution:
    def maxScore(self, s: str) -> int:
        total_count=s.count('1')
        left_zeros=0
        right_ones=total_count
        max_score=0

        for i in range(len(s)-1):
            if s[i]=='0':
                left_zeros+=1
            elif s[i]=='1':
                right_ones-=1
            else:
                i+=1
            
            score=left_zeros+right_ones
            max_score=max(max_score,score)
        return max_score
