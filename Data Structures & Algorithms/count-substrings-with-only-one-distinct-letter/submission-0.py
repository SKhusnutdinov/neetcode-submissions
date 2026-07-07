class Solution:
    def countLetters(self, s: str) -> int:
        # 2^n - 1
        run_letter = s[0]
        run_len = 1

        res = 0
        for i in range(1, len(s)):
            if s[i] != run_letter:
                run_letter = s[i]
                res += sum(i for i in range(run_len+1))
                run_len = 1
            else:
                run_len += 1

        res += sum(i for i in range(run_len+1))

        return res