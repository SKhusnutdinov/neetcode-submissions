class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            changed = False
            new_arr = arr.copy()
            for i in range(1, len(arr)-1):
                if arr[i-1] < arr[i] > arr[i+1]:
                    new_arr[i] -= 1
                    changed = True
                elif arr[i-1] > arr[i] < arr[i+1]:
                    new_arr[i] += 1
                    changed = True
            if not changed:
                return new_arr
            else:
                arr = new_arr