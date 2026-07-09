class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {
            ']':'[',
            '}':'{',
            ')':'('
            }

        for ch in s:
            if ch in [']', '}', ')']:
                if st and st[-1] == hm[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        
        return not bool(len(st))
                
                