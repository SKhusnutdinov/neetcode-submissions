class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for _ in range(k):
            curMax = 0
            for i in range(1, len(gifts)):
                if gifts[curMax] < gifts[i]:
                    curMax = i
            
            gifts[curMax] = int(sqrt(gifts[curMax]))

        return sum(gifts)