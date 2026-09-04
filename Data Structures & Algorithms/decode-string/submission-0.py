class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr=''
        num=0

        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char=='[':
                stack.append((curr,num))
                num=0
                curr=''
            elif char==']':
                pre_string,repeat=stack.pop()
                curr=pre_string+curr*repeat
            else:
                curr += char
        return curr