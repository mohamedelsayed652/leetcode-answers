class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = ""
        for i in range(len(strs[0])):#iterate through the first word
            char = strs[0][i] #char is equal to i letter of first word
            for j in range(1,len(strs)): #iterate through the rest of the list
                if i >= len(strs[j]) or strs[j][i] != char: #if mismatch is found
                    return LCP #return the Longest common prefix
            LCP = LCP + char #else add current character to the Longest common prefix
        return LCP