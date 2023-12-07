# from pathlib import Path
import  re

def prob2( data):

    for i , line in enumerate(data):
        parts = re.split("\s+" , line)
        idx = parts.index("|")
        print(idx)
        winning = list(map(int , parts[2:idx]))

if __name__ == "__main__":


    with open("/Users/itnxw/aoc2023_python/day4/data/input1.txt") as fin:
        lines = fin.read().strip().split("\n")

prob2(lines)
ans = 0

for line in lines:
    parts = re.split("\s+" , line) 
    winning =  list(map (int ,parts[2:12]))
    # print(winning)
    ours = list(map(int, parts[13:]))
    # print(ours)

    score = 0
    for num in ours:
        if num in winning:
            score += 1
    print(score)

    if score > 0:
        ans += 2**(score - 1)

print(ans)

    # filepath = str(Path.cwd()) + "/day4/data/example.txt"
    # file_hand = Path(filepath)
    # data = open(file_hand).read().strip().split('\n')
    # for line in data :
    #     parts = re.split(r"\s+",line)
    #     print(parts)
        
    #     wining= list(map(int , parts[2:12]))
    #     print(wining)

