class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True

        while changed:
            changed = False
            p = arr[0]
            for i in range(1, len(arr)-1):
                temp = arr[i]
                if p < arr[i] > arr[i+1]:
                    arr[i] -= 1
                    changed = True
                elif p > arr[i] < arr[i+1]:
                    arr[i] += 1
                    changed = True
            
                p = temp
        return arr


                    