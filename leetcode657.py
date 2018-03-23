class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for i in range(len(moves)):
            if moves[i] == 'U' :
                x -=1
            if moves[i] == 'D':
                x += 1
            if moves[i] == 'L':
                y -=1
            if moves[i] == 'R':
                y += 1
        if x==0 and y==0:
            return True
        else:
            return False
