class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {']': '[', '}': '{', ')': '('}

        for c in s:
            if c in '({[':
                stack.append(c)
                continue
            if not stack:
                return False
            
            if pairs[c] != stack.pop():
                return False

        return len(stack) == 0

