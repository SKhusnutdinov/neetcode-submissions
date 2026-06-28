class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = {}

        for ch in text:
            hm[ch] = hm.get(ch, 0) + 1
        
        return min(
            hm.get('b', 0),
            hm.get('a', 0),
            hm.get('l', 0) // 2,
            hm.get('o', 0) // 2,
            hm.get('n', 0)
        )