class Solution:
    def wordIn(self, s, word) -> bool:
        if len(s) < len(word):
            return False

        for i in range(len(word)):
            if s[i] != word[i]:
                return False

        return True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(s):
            if s == "":
                return True

            if s in memo:
                return memo[s]

            r = False

            for word in wordDict:
                if self.wordIn(s, word):
                    r = r or dfs(s[len(word):])

            memo[s] = r
            return r

        return dfs(s)