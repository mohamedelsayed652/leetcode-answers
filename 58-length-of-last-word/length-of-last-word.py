class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 1
        wordExists = False
        spaces = 0
        while n <= len(s) and (not wordExists or s[-n] != " "):
            if s[-n] == " " and wordExists == False:
                spaces = spaces + 1
            if s[-n] != " ":
                wordExists = True
            n = n + 1
        n = n - 1
        return n - spaces