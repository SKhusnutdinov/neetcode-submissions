class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            alph = [0] * 26
            for ch in word:
                alph[ord(ch) - ord('a')] += 1
            hm[tuple(alph)].append(word)
        
        return list(hm.values())