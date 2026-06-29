class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = [0] * 26

        for ch in words[0]:
            cnt[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            cur = [0] * 26

            for ch in word:
                cur[ord(ch) - ord('a')] += 1

            for i in range(26):
                cnt[i] = min(cnt[i], cur[i])

        ans = []

        for i in range(26):
            ans.extend([chr(i + ord('a'))] * cnt[i])

        return ans