class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        paths = path.split('/')

        for path in paths:
            match path:
                case '':
                    continue
                case '.':
                    continue
                case '..':
                    if st:
                        st.pop()
                case _:
                    st.append(path)
        
        return "/" + "/".join(st)