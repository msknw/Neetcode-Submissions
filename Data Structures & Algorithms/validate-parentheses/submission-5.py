class Solution:
    def isValid(self, s: str) -> bool:
        # Time:O(n)，
        # 修改点：当遇到不匹配的右括号的时候可以直接返回False
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
                        return False
                else:
                    return False
        
        return len(st) == 0