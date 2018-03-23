class Solution:
    def generateParenthesis(self, n):
        kuohao = []
        def digui(x,t,s):
            if len(s) == n * 2:
                kuohao.append(s)
            if t > x:
                if t < n:
                    digui(x,t+1,s+'(')
                digui(x+1,t,s+')')
            elif t < n:
                digui(x,t+1,s+'(')
            else:
                return
        digui(0,0,'')
        return kuohao
test = Solution()
print(test.generateParenthesis(3))