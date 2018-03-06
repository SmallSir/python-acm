









n = int(input())
a = list(map(int,input().split()))
a.append(0)
a.sort(reverse=True)
sum = 0
for i in range(n):
    if i % 2 == 0:
        sum += a[i]*a[i]-a[i+1]*a[i+1]
print(3.1415926536 * sum)


