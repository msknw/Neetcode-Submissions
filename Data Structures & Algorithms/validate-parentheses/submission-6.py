class Solution:
    def isValid(self, s: str) -> bool:
        # Time:O(n)，
        # 修改点：用mapping，不用手动写太多if
        st = []

        closeBrace = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in closeBrace:
                if st and st[-1] == closeBrace[c]:
                    st.pop()
                else:
                    return False
            
            else:
                st.append(c)
        
        return len(st) == 0