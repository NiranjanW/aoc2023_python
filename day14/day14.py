
from pathlib import Path

data = Path(__file__).with_name("example.txt").read_text().splitlines()
R=len(data)
C=len(data[0])

# for i in range(0,R):
#     for j in range(0,C):
#         print(data[i][j])

def process_column(j):
    i=0
    
    while i < R:
        while i < R and data[i][j] == "#":
            i +=1
    count = 0
    start = i

    while i <R and i < R and data[i][j] != "#":
        if data[i][j] == "0":
            count +=1
        i +=1

    for ii in range(start , start +count):
        ans += R - ii

    return ans 

ans = 0

for j in range(C):
    ans += process_column(j)

print(ans)

    
        
# print(data, R,C)