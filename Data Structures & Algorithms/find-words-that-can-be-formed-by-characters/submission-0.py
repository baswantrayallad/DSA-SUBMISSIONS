class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count=[0]*26

        for ch in chars:
            char_count[ord(ch)-ord("a")]+=1

        total=0

        for word in words:
            temp=char_count.copy()

            for ch in word:
                index= ord(ch)-ord("a")

                if temp[index]==0:
                    break
                temp[index]-=1
            else:
                total+=len(word)
        return total