
from pathlib import Path
import re

def ways (t,d) :
    count = 0
    for i in range(t):
        if (t-i) * i > d:
            count +=1
    return count

if __name__ == "__main__":

    filepath = str(Path.cwd()) + "/day6/data/input.txt"
    file_hand = Path(filepath)
    data = open(file_hand).read().strip().split('\n')
    
    times = list(map(int, data[0].split()[1:]))
    distances = list(map(int, data[1].split()[1:]))

    # print(times)
    # times = [ print( line) for line in data[0].split()[:]]

    ans = []
    for t ,d in zip(times ,distances):
        ans.append(ways(t,d))
    print(ans)

    p = 1
    for x in ans:
         p *= x
print(p)