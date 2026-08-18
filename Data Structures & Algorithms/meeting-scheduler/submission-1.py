class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        l = r = 0

        while l < len(slots1) and r < len(slots2):
            start = max(slots1[l][0], slots2[r][0])
            end = min(slots1[l][1], slots2[r][1])

            if end - start >= duration:
                return [start, start + duration]
            
            if slots1[l][1] < slots2[r][1]:
                l += 1
            else:
                r += 1
        
        return []
            