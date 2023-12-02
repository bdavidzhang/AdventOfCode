import sys
D = open(sys.argv[1]).read().strip()

ans = 0

# 12,13,14
for line in D.split('\n'):
    flag = 0
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
            if (rc > 12 or bc > 14 or gc > 13):
                flag = -1
    if flag == 0:
        ans += val
    if flag == -1:
        print(val) 
        
                        
print(ans)
