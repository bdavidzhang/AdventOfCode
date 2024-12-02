from math import *
f = open("d2/data.txt","r")
s = f.read().split('\n')

def solve1():
    ans = 0
    for r in s: 
        a = [int(c) for c in r.split()]
        print(a)
        cur = a[1]
        pre = a[0]
        dif = a[1]-a[0]
        flag = dif != 0 and (abs(dif) >= 1 and abs(dif) <= 3 ) 
        for i in range(2,len(a)):
            cur = a[i]
            pre = a[i-1]
            if dif * (cur-pre) > 0:
                dif = cur - pre
                if(abs(dif) < 1 or abs(dif) > 3 ):
                    flag = False
                    break
            else:
                flag = False
                break
        
        if flag:
            print(a)
            ans += 1
    return ans 

#solvable by brute force (O(n) also exists)

def getflag(a):
    cur = a[1]
    pre = a[0]
    dif = a[1]-a[0]
    flag = dif != 0 and (abs(dif) >= 1 and abs(dif) <= 3) 
    for i in range(2,len(a)):
        cur = a[i]
        pre = a[i-1]
        if dif * (cur-pre) > 0:
            dif = cur - pre
            if(abs(dif) < 1 or abs(dif) > 3 ):
                flag = False
                break
        else:
            flag = False
            break
    return flag 

def solve2():
    ans = 0
    for r in s: 
        a = [int(c) for c in r.split()]
        
        print(a)
        cur = a[1]
        pre = a[0]
        dif = a[1]-a[0]
        flag = dif != 0 and (abs(dif) >= 1 and abs(dif) <= 3 ) 
        for i in range(2,len(a)):
            cur = a[i]
            pre = a[i-1]
            if dif * (cur-pre) > 0:
                dif = cur - pre
                if(abs(dif) < 1 or abs(dif) > 3 ):
                    flag = False
                    break
            else:
                flag = False
                break
        
        if flag:
            ans += 1
        else:
            Flag = False
            for i in range(len(a)):
                b = [x for x in a]
                b.pop(i)
                Flag = Flag or getflag(b)
            if Flag:
                print(a)
                ans += 1
    return ans  
    
ans = solve2()
print(ans)
        
        