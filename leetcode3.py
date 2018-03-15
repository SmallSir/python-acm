class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        check = {}
        start = 0
        MAX = 0
        for i in range(n):
            if s[i] in check and check[s[i]] >= start:
                start = check[s[i]] + 1
            MAX = max(MAX,i - start + 1)
            check[s[i]] = i
        return MAX
test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))