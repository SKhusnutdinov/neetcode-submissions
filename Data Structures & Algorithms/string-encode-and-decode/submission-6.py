class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        count = 0
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                res.append(s[i+1:i+count+1])
                i += count
                count = 0
            else:
                count = count * 10 + int(s[i])
            i += 1
        return res