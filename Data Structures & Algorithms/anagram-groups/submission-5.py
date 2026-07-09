class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for ch in word:
                alpha[ord(ch) - ord('a')] += 1
            hm[tuple(alpha)].append(word)
        
        return list(hm.values())