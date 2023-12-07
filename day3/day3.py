from pathlib import Path



def main():
    pass

def sol1(data):
    G =data
    print(G)
    for r , row in enumerate(G):
        for c , ch in enumerate(row):
            if ch.isdigit() or ch == '.':
                continue
            for cr in [r-1 ,r,r+1]:
                for cc in [c-1,c,c+1]:
                    if cr <0
            else:
                print(ch)


if __name__ == "__main__":
    file_path = str(Path.cwd()) + "/day3/data/example.txt"
    file = Path(file_path)
    data = open(file).read().strip()
    
    lines =  data.split('\n')
    sol1(lines)
    # G = [ [c for c in line ] for line in lines ]   
    # # print(G)
    # for r in range(len(G)):
    #     for c in range(len(G[r])):
    #         if G[r][c].isdigit():
    #             print(G[r][c])

