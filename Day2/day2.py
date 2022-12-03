with open('Day2/day2.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# Code for part one
# cnt = 0
# for i in data:
#     if (i[0] == 'A'):
#         if (i[2] == 'X'):
#             cnt += 1+3
#         elif (i[2] == 'Y'):
#             cnt +=  2+6
#         else: 
#             cnt += 3+0
#     elif (i[0] == 'B'):
#         if (i[2] == 'X'):
#             cnt += 1+0
#         elif (i[2] == 'Y'):
#             cnt +=  2+3
#         else: 
#             cnt += 3+6
#     elif (i[0] == 'C'):
#         if (i[2] == 'X'):
#             cnt += 1+6
#         elif (i[2] == 'Y'):
#             cnt +=  2+0
#         else: 
#             cnt += 3+3    

# print(cnt)

cnt = 0 
for i in data:
    if (i[0] == 'A'):
        if (i[2] == 'X'):
            cnt += 0+3
        elif (i[2] == 'Y'):
            cnt += 3+1
        else:
            cnt += 6+2
    elif (i[0] == 'B'):
        if (i[2] == 'X'):
            cnt += 0+1
        elif (i[2] == 'Y'):
            cnt += 3+2
        else:
            cnt += 6+3
    elif (i[0] == 'C'):
        if (i[2] == 'X'):
            cnt += 0+2
        elif (i[2] == 'Y'):
            cnt += 3+3
        else: 
            cnt += 6+1  
print(cnt)
