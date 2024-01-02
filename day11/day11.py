from pathlib import Path
import re

# for m in re.finditer('#' ,)

lines = Path(__file__).with_name("example.txt").read_text().split('\n')
n ,m = len(lines) , len(lines[0])

coords =[]
for i in range(n):
    for j in range(m):
        if lines[i][j] == "#":
            print("Found")
            coords.append((i,j))

N = len(coords)

print(N)

empty_row = [ all(lines[i][j] == "." for j in range( m))for i in range(n)]
empty_col = [all([lines[i][j] == "." for i in range(n)]) for j in range(m)]



def dist(a,b):
    i1, j1 = a
    i2, j2 = b

    i1, i2 = min(i1,i2) , max(i1,i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1,i2):
        ans +=1
        if empty_row[i]:
            ans += 1
    for j in range(j1, j2):
        ans += 1
        if empty_col[j]:
            ans += 1

    return ans
        

ans = 0
for idx in range(N):
    for idx1 in range(idx+1,N):
        d =dist(coords(idx, coords(idx1)))
        ans +=d

# count= 0 
# for i , line in enumerate(lines):
#     # print(line)
#     for m in re.findall('#' , line):
#         print(m)

#     if '#' in line:
#         print(i , line)
#         count +=1
# print(count)