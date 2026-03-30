class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
                maping_stot={}
                maping_ttos={}
                for i in range(len(s)):
                    char_s=s[i]
                    char_t=t[i]

                    if char_s in maping_stot:
                        if maping_stot[char_s]!=char_t:
                            return False
                    else:
                        maping_stot[char_s]=char_t

                    if char_t in maping_ttos:
                        if maping_ttos[char_t]!=char_s:
                            return False                                                                     
                    else:                                                                                                                                        
                         maping_ttos[char_t]=char_s
                return True
 
        