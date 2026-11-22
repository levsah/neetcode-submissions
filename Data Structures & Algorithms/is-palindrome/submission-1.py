class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpaces = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(noSpaces) - 1
        
        while l < r:
            if noSpaces[l] != noSpaces[r]:
                return False
            l += 1
            r -= 1
        return True

        