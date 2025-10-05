class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x > 0:
            return True
        num = str(x)
        reversedNum = num[::-1]
        if num == reversedNum:
            return True
        return False