from re import *
from math import *
with open("d3/data.txt", "r") as f:
    s = f.read()


def solve1(s):
    num = r"mul\((\d+),(\d+)\)"
    res = findall(num,s)
    ans = 0
    for a in res:
        ans += int(a[0]) * int(a[1])

    print(ans)

def solve2():
    d0 = r"do\(\)"
    d1 = r"don't\(\)"
    p0 = [(0,1)]
    p1 = []
    for m in finditer(d0,s):
        p0.append((m.start(),1))
    for m in finditer(d1,s):
        p1.append((m.start(),2))
    p = p0 + p1
    p.sort(key=lambda x : x[0])
    p.append((len(s)-1,p[-1][1]))
    strs = []
    for i in range(len(p)-1):
        if p[i][1] == 1:
            strs.append(s[p[i][0]:p[i+1][0]])
    t = "".join(strs)
    solve1(t)
        

solve2()