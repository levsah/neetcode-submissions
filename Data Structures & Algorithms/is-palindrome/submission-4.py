class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = [ch.lower() for ch in s if ch.isalnum()]

        l, r = 0, len(lowered) - 1
        while l < r:
            if lowered[l] != lowered[r]:
                return False
            l +=1 
            r -= 1
        return True
        