a =[]
for i in range(3):
    a.append(list(map(int,input().split())))
a[1][1] = int(( a[0][1] + a[0][2] + a[2][0] + a[2][1] - a[1][0] - a[1][2] )/2)
a[0][0] = int(a[1][0] + a[1][1] + a[1][2] - a[0][1] -a[0][2])
a[2][2] = int(a[1][0] + a[1][1] + a[1][2] - a[2][1] -a[2][0])
for i in range(3):
    print(a[i][0],a[i][1],a[i][2])
