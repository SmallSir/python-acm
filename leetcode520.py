class Solution:
    def detectCapitalUse(self, word):
        flag = []
        for i in range(len(word)):
            if word[i] >= 'A' and word[i] <= 'Z':
                flag.append(i)
        if len(flag) == len(word) or len(flag) == 0 or (len(flag) == 1 and flag[0] == 0):
            return True
        else:
            return False