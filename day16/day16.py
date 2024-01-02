from pathlib import Path

lines = Path(__file__).with_name("example.txt").read_text().split('\n')
G = [[c for c in line] for line in lines ]
# print(G)
R = len(G)
C=len(G[0])

DR = [-1 ,0 ,1,0]
DC =[0,1,0,-1]
POS=[0,0,1]
SEEN = set()

while True:
    NP=[]
    if not POS:
        break
    for (r,c,d) in POS:
        print(r,c,d)
        SEEN.add((r,c))
        rr = r+DR([d])
        cc =  c+DC([d])

        if 0<=rr<R and 0<=cc<C:
            ch = G[rr][cc]
            if ch =='.':
                NP.append(r,c,d)
            elif ch =='/':
                # up , right , down left
                NP.append((rr,cc,{0:1, 1:0 , 2:3, 3:2}[d]))
            elif ch =='\\':
                # up , right , down left
                NP.append((rr,cc,{0:1, 1:0 , 2:3, 3:2}[d]))
            elif ch =='/':
                # up , right , down left
                NP.append((rr,cc,{0:1, 1:0 , 2:3, 3:2}[d]))

         
         
print(R,C)