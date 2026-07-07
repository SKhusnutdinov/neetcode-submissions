class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = -1
        cand2 = -1

        freq1 = 0
        freq2 = 0

        for num in nums:
            if num == cand1:
                freq1 += 1
            elif num == cand2:
                freq2 += 1
            elif freq1 == 0:
                cand1 = num
                freq1 = 1
            elif freq2 == 0:
                cand2 = num
                freq2 = 1
            else:
                freq1 -= 1
                freq2 -= 1
        
        freq1 = freq2 = 0

        for num in nums:
            if num == cand1:
                freq1 += 1
            elif num == cand2:
                freq2 += 1
        
        res = []
        

        if freq1 > len(nums) // 3:
            res.append(cand1)
        if freq2 > len(nums) // 3:
            res.append(cand2)
        
        return res