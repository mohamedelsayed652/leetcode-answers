class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
            }
        stack = []

        for i in s:
            if i in pairs.values(): #if its opening append it to stack
                stack.append(i)
            elif i in pairs.keys() : #if its closing
                if not stack or stack[-1] != pairs[i]: #if stack is empty or current closing parenthesis isnt the right one
                    return False
                stack.pop() #if it passes those checks, pop the last character off stack
            else:
                return False #if invalid character
        return len(stack) == 0 #if stack is empty return true otherwise return false