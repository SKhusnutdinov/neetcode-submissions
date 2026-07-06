class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opn = 0
        st = []

        for ch in s:
            if ch == '(':
                opn += 1
                st.append(ch)
            elif ch == ')':
                if opn > 0:
                    opn -= 1
                    st.append(ch)
            else:
                st.append(ch)
        
        filt = []

        for c in reversed(st):
            if c == "(" and opn > 0:
                opn -= 1
            else:
                filt.append(c)

        
        return "".join(reversed(filt))