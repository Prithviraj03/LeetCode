class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        All = False
        for i in range(len(strs[0])):
            word = strs[0][i] #f #l ...

            if all(len(word) > i and word[i] == strs[0][i] for word in strs):
                res += strs[0][i]
            else:
                return res
        return res