class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            match op:
                case "+":
                    st.append(st[-1] + st[-2])
                case "D":
                    st.append(st[-1] * 2)
                case "C":
                    st.pop()
                case _:
                    st.append(int(op))
            print(st)
        return sum(st)