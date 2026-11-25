class Solution:
    def isValid(self, s: str) -> bool: 
        bank = {'{':'}', '(':')', '[':']'}
        stack = []
        for ch in s:
            ## ch is an opener, in the keys of bank
            if ch in bank:
                stack.append(ch)
            
            ## ch must be a closer
            ## if the stack is empty, you can't add a closer here
            elif not stack or ch != bank[stack[-1]]:
                return False
            else:
                stack.pop()

        if len(stack) != 0:
            return False
        return True 
        