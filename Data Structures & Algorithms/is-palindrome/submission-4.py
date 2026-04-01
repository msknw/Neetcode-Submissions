class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 直接用[::-1]
        if not s:
            return True

        tmps = ""
        for c in s:
            if c.isalnum():
                tmps += c.lower()

        return tmps == tmps[::-1]