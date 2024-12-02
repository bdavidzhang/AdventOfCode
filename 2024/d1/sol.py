from math import *
f = open("d1/test.txt","r")
s = f.read().split('\n')

a = []
b = []
for _ in s: 
    l = _.split("   ")
    a.append(l[0])
    b.append(l[1])

d1 = {}
d2 = {}

for _ in a:
    if(not _ in d1):
        d1[_] = 1
    else:
        d1[_]+=1

for _ in b:
    if(not _ in d2):
        d2[_] = 1
    else:
        d2[_]+=1

ans = 0

for keys in d1:
    if(not keys in d2):
        continue
    ans += int(keys)*d1[keys]*d2[keys]


print(ans)