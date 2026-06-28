class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        maxCount = 0

        for i in range(len(flowerbed)):
            cur = flowerbed[i]
            if i-1 == -1:
                prev = 0
            else:
                prev = flowerbed[i-1]
            
            if i+1 == len(flowerbed):
                next = 0
            else:
                next = flowerbed[i+1]
            
            if cur + prev + next == 0:
                flowerbed[i] = 1
                maxCount += 1
        
        return maxCount >= n