class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        st = [] # pair (temp, idx)

        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                res[st[-1][1]] = i - st[-1][1]
                st.pop()
            st.append((temp, i))
        
        return res