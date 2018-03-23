with open(r'1.png','rb') as f:
    a = []
    l = h = 0
    MAX = 0
    for s in str(f.read()).split("\\"):
         #if len(s) == 0 and s[0] =='n':
         #    MAX=max(l,MAX)
         #    h+=1
         #    l=0
         if len(s) >= 3 and s[0] == 'x':
            a.append(str(0)+s[:3])
            l+=1
with open('text.txt','a') as f:
    for i in range(len(a)):
        f.write(a[i]+',')
print(len(a))
print(l,h)


