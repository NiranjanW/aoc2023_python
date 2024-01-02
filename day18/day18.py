from pathlib import Path

# def lava(cor):
#     matrix = []
#     direct  , depth = [ seq[0] seq[1] for seq in cor]
#     print(direct )
    # unzipped = zip(*cor)
    # print(unzipped)
    # for x in coord:
    #    if x[0] == 'R':
    #        for i in x[1]:
    #            print('#')
    #     #    print(''.join)


if __name__ == "__main__":

    filepath = str(Path.cwd()) + "/day18/example.txt"
    file_hand = Path(filepath)
    with open( file_hand )as f:
        lines = f.readlines()
    g = set()
    cx , cy = 0 , 0    
    for line in lines:
         line.split("\n")
        #  print(line)
         dir , x, col = line.split()
         dx , dy = {
             "R" : (0,1),
             "D" : (1,0),
             "U" : ( -1 ,0),
             "L" :( 0 , -1)
             
         }[dir]
         for _ in range(int(x)):
             g.add((cx ,cy))
             cx += dx
             cy += dy
         g.add((cx, cy))
    sx , sy = (-1,1)
    assert (sx ,sy) not in g
    print(g ,len(g))
        
             
            
    # coord = []
    # for line in data:
    #     direct , depth = line.split()[0], int(line.split()[1])
    #     coord.append((direct , depth))
    
    # lava(coord)