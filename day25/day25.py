
from pathlib import Path
from collections import defaultdict , deque

lines = Path(__file__).with_name("example.txt").read_text().split('\n')

E = defaultdict(list)
E2=[]

for line in lines:
    s, e = line.split(":")
    for y in e.split():
        E[s].append(y)
        E2.append((s,e))
start = list(E.keys())[0]
# for y in E['jqt']:
#     print(y)
# print(E)
n = len(E)

for e1 in E2:
    for e2 in E2:
        for e3 in E2:
            # print( e1,e2,e3)
            Q = deque([start])
            # print(Q)
            SEEN = set()
            while Q:
                x = Q.popleft()
                if x in SEEN:
                    continue
                SEEN.add(x)
                for y in E[x]:
                    if (x,y) not in [e1,e2,e3] and (y,x) not in [e1,e2,e3]:
                        Q.append(y)
            if len(SEEN) < n:
                n1 = len(SEEN)
                n2 = n -len(SEEN)
                print(e1,e2,e3, n1,n2)
                print(n1,n2)
    # print(e1)



#     k ,v = line[0] ,line[:]
#     wires[k] = wires[v]

# for k , v in wires.items():
#     print(k ,v)


