class Solution:
    def isValid(self, s: str) -> bool:
        # Time:O(n)，但又更快的改进
        st = []

        for c in s:
            if c == '[' or c == '(' or c == '{':
                st.append(c)
            else:
                if st:
                    if c == ']' and st[-1] == '[':
                        st.pop()
                    elif c == ')' and st[-1] == '(':
                        st.pop()
                    elif c == '}' and st[-1] == '{':
                        st.pop()
                    else:
                        st.append(c)
                else:
                    st.append(c)
        
        return len(st) == 0