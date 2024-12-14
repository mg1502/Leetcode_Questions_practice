class Solution:
    def isValid(self, s: str) -> bool:  # Rename to isValid
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0

# Example usage
sol = Solution()
print(sol.isValid("()"))       # True
print(sol.isValid("()[]{}"))   # True
print(sol.isValid("(]"))       # False
print(sol.isValid("([])"))     # True
