import sys
D = open(sys.argv[1]).read().strip()

ans = 0

for line in D.split('\n'):
    minr = 0
    ming = 0
    minb = 0
    a = line.split(' ')
    val = int(a[1].replace(':',''))
    index = [2]
    for i,s in enumerate(a):
        if s.find(';') != -1:
            index.append(i)
            a[i] = a[i].replace(';','')
        if s.find(',') != -1:
            a[i] = a[i].replace(',','')
    index.append(len(a)-1)
    print(index)
    print(a)

    for i in range(len(index)-1):
        for j in range(index[i],index[i+1]):
            rc = bc = gc = 0
            if a[j].isdigit():
                if (a[j+1] == 'red'):
                    rc += int(a[j])
                elif (a[j+1] == 'blue'):
                    bc += int(a[j])
                else:
                    gc += int(a[j])
            if (minr < rc): 
                minr = rc
            if (minb < bc):
                minb = bc
            if (ming < gc):
                ming = gc


    ans += minr*ming*minb 
                        
print(ans)
