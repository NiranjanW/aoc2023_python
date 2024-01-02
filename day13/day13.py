from pathlib import Path

with open("/Users/itnxw/aoc2023_python/day13/example.txt") as f:
    s = f.read().strip()

qs = s.split("\n\n")

print(qs)
# lines = Path(__file__).with_name("example.txt").read_text().split('\n\n')
# # qs = line
# G = [[c for c in line] for line in lines ]
# # print(G)
# R = len(G)
# C=len(G[0])
# ans=[]


# def check_row(g,n,m,i):
#     for x in range(n):
#         for y in range(m):
#             nx , ny = i+1 +(i-x) , y
#             if g[x][y] != g[nx][ny]:
#                 return False
#     return True

# for i in range(0,R-1):
#     # print(G,R,C,i)
#     if check_row(G,R,C,i):
#         ans.append[R]
# print(ans)
#     # for j in range(C):
#     #     print(G[i][j])