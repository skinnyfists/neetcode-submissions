class Solution:
    BRACKET_MAP = {")": "(", "}": "{", "]": "["}
    def isValid(self, s: str) -> bool:

        stack = []
        for bracket in s:
            if bracket in self.BRACKET_MAP:
                if stack and self.BRACKET_MAP[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack
