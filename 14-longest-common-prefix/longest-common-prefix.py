class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            match = True
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i] :
                    match = False
                    break

            if match:
                res += strs[0][i]
            else:
                break

        return res