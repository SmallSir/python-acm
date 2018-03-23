class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        minL = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(minL):
                minL = strs[i]
        for i in range(len(strs)):
            for j in range(len(minL)):
                if minL[j] != strs[i][j]:
                    minL = minL[:j]
                    break
        return minL