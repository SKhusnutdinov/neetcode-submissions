class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = set()
        for word in words:
            for wor in words:
                if word != wor and word in wor:
                    arr.add(word)

        return list(arr)