class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if not needle:
            return index
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] == needle[0]:
                index = i
                for j in range(1,len(needle)):
                    if haystack[i+j] != needle[j]:
                        index = -1
                        break
            if index != -1:
                return index
        return index