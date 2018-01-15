import string
n,m = map(int,input().split())
a=[]
b=[]
x=[]
y=[]
for i in range(n):
    a.append(input())
    x.append(False)
for j in range(m):
    b.append(input())
    y.append(False)

cnt = 0
for i in range(n):
    for j in range(m):
        if a[i] == b[j] and x[i] == False and y[j] == False:
            cnt+=1
            x[i] =True
            y[j]= True
if n-cnt == m - cnt:
    if cnt % 2 == 0:
        print("No")
    else:
        print("Yes")

else:
    if n-cnt > m - cnt:
        print("Yes")
    else:
        print("No")