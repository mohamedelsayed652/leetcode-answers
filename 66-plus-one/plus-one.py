class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 1
        while n < len(digits):
            if digits[-n] == 9:
                digits[-n] = 0
                n = n + 1
            else:
                digits[-n] = digits[-n] + 1
                return digits
        if digits[0] == 9:
            digits[0] = 1
            digits.append(0)

        elif digits[0] != 9:
            digits[0] = digits[0] + 1
        return digits