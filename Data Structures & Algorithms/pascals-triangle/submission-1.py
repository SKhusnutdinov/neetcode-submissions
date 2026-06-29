class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(1, numRows):
            new = [0] * (len(res[-1]) + 1)
            for i in range(len(new)):
                if i == 0 or i == len(new) - 1:
                    new[i] = 1
                else:
                    new[i] = res[-1][i] + res[-1][i-1]
            res.append(new)
        
        return res