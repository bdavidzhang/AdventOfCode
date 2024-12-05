f = open('d5/data.txt','r')
s = f.read().strip().split('\n')
items = set({})
for l in s:
    a = l.split('|')
    items.add(a[0])
    items.add(a[1])
   
n = int(max(items))
print(n)
ord = [[0 for _ in range(n+1)] for _ in range(n+1)]

for l in s:
    a = l.split('|')
    ord[int(a[1])][int(a[0])] = -1
    ord[int(a[0])][int(a[1])] = 1
#now we have graph stored in adj matrix

g = open('d5/data2.txt','r')
s = g.read().strip().split('\n')

def solve1():
    ans = 0
    for l in s:
        a = [int(c) for c in l.split(',')]
        n = len(a)
        f = True
        for i in range(n):
            for j in range(i,n):
                if(ord[a[i]][a[j]] == -1):
                    f = False
                    break
        if(f):
            ans += a[(n)//2]
            print(a)
    return ans

def solve2():
    ans = 0
    for l in s:
        a = [int(c) for c in l.split(',')]
        n = len(a)
        f = True
        freq = []
        for i in range(n):
            for j in range(i,n):
                if(ord[a[i]][a[j]] == -1):
                    f = False
                    break
               
        if(not f):
            for i in range(n):
                cnt = 0
                for j in range(n):
                    if(ord[a[i]][a[j]] == -1):
                        f = False
                    elif (ord[a[i]][a[j]] == 1):
                        cnt += 1
                freq.append((cnt,i))
            freq.sort(key=lambda x : x[0],reverse=True)
            t = [a[b[1]] for b in freq]
            print(t)
            ans += t[n//2]
            
    return ans 

ans = solve2()
print(ans)

