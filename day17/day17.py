from pathlib import Path
from collections import defaultdict, Counter , deque
import heapq
import pysnooper


lines = Path(__file__).with_name("example.txt").read_text().split('\n')
G = [[c for c in line] for line in lines ]

Q = [(0,0,0,-1,-1)]
D = {}
R = len(G)
C = len(G[0])
# with pysnooper.snoop():

while Q:
    dist,r,c,dir_ , indir = heapq.heappop(Q)
    if (r,c,dir_, indir) in D:
        assert dist >= D[(r,c,dir_,indir)]
        continue
    D[(r,c,dir_,indir)] = dist
    for i , (dr,dc) in enumerate([[-1,0], [0,1],[1,0],[0,-1]]):
        rr = r + dr
        cc = c + dc
        new_dir = i
        new_indir = ( 1 if  new_dir!=dir_ else indir+1)
        isnt_reverse = ((new_dir + 2)%4 != dir_)

        isvalid_part1 = (new_indir<=3)
        isnt_reverse = ((new_dir + 2)%4 != dir_)

        if 0<=rr<R and 0<=cc<C and isvalid_part1 and isnt_reverse:
            cost = int(G[rr][cc])
            if (rr,cc,new_dir,new_indir) in D:
                continue
            heapq.heappush(Q,(dist+cost , rr,cc,new_dir,new_indir))    
ans = 1e9
for (r,c,dir_,indir) , v in D.items():
    if r==R-1 and c==C-1:
        ans = min(ans,v)
print(ans)



