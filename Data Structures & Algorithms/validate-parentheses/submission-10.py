class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bank = {'{':'}', '[':']', '(':')'}

        for ch in s:
            ## opening bracket
            if ch in bank:
                stack.append(ch)
            ## closing bracket
            elif not stack or ch != bank[stack[-1]]:
                return False
            else:
                stack.pop()

        if len(stack) != 0:
            return False

        return True

        