class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for ch in tokens:
            print(st)
            match ch:
                case "+":
                    st.append(st.pop() + st.pop())
                case "*":
                    st.append(st.pop() * st.pop())
                case "-":
                    a = st.pop()
                    b = st.pop()
                    st.append(b - a)
                case "/":
                    a = st.pop()
                    b = st.pop()
                    print(a, b)
                    st.append(int(b/a))
                case _:
                    st.append(int(ch))
            
        return st[-1]