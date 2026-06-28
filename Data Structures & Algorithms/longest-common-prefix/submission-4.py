class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie()

        for word in strs:
            cur = root

            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Trie()
                cur = cur.children[ch]
            
            cur.is_end = True
        
        pr = []

        cur = root

        while len(cur.children) == 1 and not cur.is_end:
            ch = next(iter(cur.children))
            pr.append(ch)
            cur = cur.children[ch]
        
        return "".join(pr)
