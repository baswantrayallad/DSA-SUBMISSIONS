class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res_allowed=set(allowed)
        count=0

        for word in words:
            is_valid=True

            for ch in word:
                if ch not in res_allowed:
                    is_valid=False
                    break
            if is_valid==True:
                count+=1
        return count