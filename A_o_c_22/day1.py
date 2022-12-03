#I need to learn how to read input this way"
with open('day1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

cnt = 0
max = 0
#this is a totals list
totals = []
for i in data:
    if i == '':
        totals.append(cnt)
        cnt = 0
    else:
        cnt += int(i)
#sort the total amount of calories each elf has, and then print the maximum & 2nd & 3rd greatet maximums
stot = sorted(totals)
print(stot[-1])
print(sum(stot[-3:]))