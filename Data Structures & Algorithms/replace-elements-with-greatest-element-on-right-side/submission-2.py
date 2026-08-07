class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)

        for i in range(n):
            tot=-1
            for j in range(i+1, n):
                if arr[j]>tot:
                    tot =arr[j]
            arr[i]=tot
        return arr
