from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # find the minimum length of all strings
        min_len = min(len(s) for s in strs)
        
        # iterate over characters of the first string
        for i in range(min_len):
            c = strs[0][i]
            # check if all other strings have the same character
            if not all(s[i] == c for s in strs[1:]):
                return strs[0][:i]
        
        return strs[0][:min_len]
#c2 xin vcl dung *str
"""
strs = ["flower","flow","flight"]
l = list(zip(*strs))
>>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
