def rucksack(input_file):
    cnt = 0 
    with open(input_file) as f:
        for lines in f.readlines():
            inline = [a for a in lines.rstrip()] 
            part1 = set(inline[0:len(inline)//2])
            part2 = set(inline[len(inline)//2:len(inline)])
            sol = list(part1.intersection(part2))[0]
            val = ord(sol)-96 if sol.islower() else ord(sol)-38
            cnt += val
    return cnt

def rucksack2(input_file):
    cnt = 0
    num = 0
    commonbadge = set()
    with open(input_file) as f:
        for lines in f.readlines():
            badge = set([a for a in lines.rstrip()]) 
            num += 1
            commonbadge = badge if num % 3 == 1 else commonbadge.intersection(badge)
            
            if (num % 3 == 0):
                sol = list(commonbadge)[0]
                commonbadge = set()
                val = ord(sol)-96 if sol.islower() else ord(sol)-38
                cnt += val
    return cnt




print(rucksack('testday3.in'))
print(rucksack('day3.in'))
print(rucksack2('testday3.in'))
print(rucksack2('day3.in'))

# i = data[0]
# #CjhshBJCSrTTsLwqwqwb
# l = len(i)
# for j in range (int(l/2)+1,l):
#     if i[j] in i[0:int(l/2)]:
#         if i[j].islower():
#             cnt += ord(i[j])-96
#         else:
#             cnt += ord(i[j])-38
# print(cnt)
# print(i[0:int(l/2)])
# print(i[int(l/2):l+1])