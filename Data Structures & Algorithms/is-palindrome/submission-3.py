class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)

        i = 0
        j = n - 1
        while (i <= j):
            print(i,j)
            if not self.isalphaNum(s[i]):
                i += 1
                continue
            if not self.isalphaNum(s[j]):
                j -= 1
                continue
            
            if (s[i].lower() != s[j].lower()):
                return False
            
            i += 1
            j -= 1
        
        return True

    def isalphaNum(self ,c):
        return ((c >= 'a' and c <= 'z')
                or (c >= 'A' and c <= 'Z')
                or (c >= '0' and c <= '9'))