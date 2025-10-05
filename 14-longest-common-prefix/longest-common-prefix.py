class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = ""

        for i in range(len(strs[0])): # iterate the first word's letters
            char = strs[0][i]                # pick current character
            for word in strs[1:]:            # compare with all other words
                if i >= len(word) or word[i] != char:
                    return prefix             # mismatch
            prefix += char                    
        
        return prefix