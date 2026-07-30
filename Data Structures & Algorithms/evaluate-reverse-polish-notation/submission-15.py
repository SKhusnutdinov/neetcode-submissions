class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for tok in tokens:
            if tok in ['+', '-', '*', '/']:
                b = st.pop()
                a = st.pop()
                res = 0
                if tok == '+':
                    res = a + b
                elif tok == '-':
                    res = a - b
                elif tok == '*':
                    res = a * b
                else:
                    res = int(a / b)
                
                st.append(res)
            else:
                st.append(int(tok))
        
        return st[-1]