import string
str1 = input()
str2 = input()
n=len(str1)
flag = 0
str1 = str1[:n-1] + chr(ord(str1[n-1])+1)
for i in range(n):
    if str1[n-i-1] > 'z' :
        str1 = str1[:n-i-1]+ 'a'+str1[n-i:]
        str1=  str1[:n-i-2]+chr(ord(str1[n-i-2])+1)+str1[n-i-1:]
if str1 < str2 and flag == 0:
    print(str1)
else:
    print("No such string")
