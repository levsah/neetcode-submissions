class Solution:
    def isValid(self, s: str) -> bool:
        bank = {'[':']', '{':'}', '(':')'}
        stack = []

        for ch in s:
            if ch in bank:
                stack.append(ch)
            elif not stack or bank[stack[-1]] != ch:
                return False
            else: 
                stack.pop()
        
        if len(stack) != 0:
            return False

        return True

            
        
        