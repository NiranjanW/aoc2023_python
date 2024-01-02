from pathlib import Path
from itertools import groupby
import itertools


lines = Path(__file__).with_name("example.txt").read_text().split('\n')

def group(vv):
    gr = []

ans = 0

def nums (a):
    return a.split(",")

for line in lines:
    a, b = line.split()
    # print(a)
    # print(b)
    g = nums(b)
    qpos = [ i for i in range(a) if a[i] == "?"]
    q = list(a)
    pos= 0 
    for qf in itertools.product( * [ "#." for _ in qpos]):
        for i ,v in zip(qpos , qf):
            q[i] = v
        if group(q) == g:
            pos += 1
    ans += poss
groups = groupby(a)   
[print(label , sum( 1 for _ in group) ) for label , group in groups] 
  