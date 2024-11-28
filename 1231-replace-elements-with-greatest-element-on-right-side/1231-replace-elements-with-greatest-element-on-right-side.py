class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        high = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = high
            high = max(high, temp)
        arr[-1] = -1
        return arr