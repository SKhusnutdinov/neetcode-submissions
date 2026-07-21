class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        pref = [0] * len(height)
        suf = [0] * len(height)
        pref[0] = height[0]
        suf[-1] = height[-1]

        for i in range(1, len(height)):
            pref[i] = max(pref[i-1], height[i])
        for j in range(len(height) - 2, -1, -1):
            suf[j] = max(suf[j+1], height[j])
        for k in range(1, len(height) - 1):
            res += (min(pref[k], suf[k]) - height[k])
        
        return res