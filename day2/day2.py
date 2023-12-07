import io
from pathlib import Path
from collections import defaultdict
import re
# import pandas as pd
            
def prob1(data):
     ans = 0
     for line in data.split('\n'):
        status = True
        id, game = line.split(':')
        for event in game.split(';'):
            for balls in event.split(','):
                   num ,color= balls.split()
                   if int(num) > {'red':12 , 'green':13 , 'blue':14}.get(color,0):
                        status = False
        if status:
             game_num = int(id.split()[-1])
            #  print(game_num)
             ans += (game_num)
     print(ans)


def prob2(data):
    #  game_cube = {'red':0 , 'green':0 , 'blue':0}
     for line in data.split('\n'):
        status =  True
        id, game = line.split(':')

        game_cube= defaultdict(int)
        for event in game.split(';'):
            for balls in event.split(','):
                   num ,color = balls.split()
                #    if color not in game_cube:
                #         game_cube[color] = int(num)
                   num = int(num)
                   game_cube[color] = max(game_cube[color] , num) 

                   if int(num) > {'red':12 , 'green':13 , 'blue':14}.get(color,0):
                    status = False
        print(game_cube)
        sum = 1
        for v in game_cube.values():
            sum *= v
        print (sum)

        if status:
            pass
    #     if status:
    #          game_num = int(id.split()[-1])
    #         #  print(game_num)
    #          ans += (game_num)
    #  print(ans)
     
     pass
     
    # print(data)
    # with open(file , 'r') as f:


if __name__ == '__main__' :
    file_path = str(Path.cwd())+"/day2/data/example.txt"
    file = Path(file_path)
   
    data = open(file).read().strip()
    # prob1(data)
    # prob2(data)

    games = re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)', data)
    print(games)
    #     # lines = [ print(line.strip()) for line in f]
    #     lines = [ line.strip().split(';')for line in f]
    # for line in lines:
    #     line.split(',')
    #     print(line)
    # df = pd.read_csv(io.StringIO(lines) , delimiter=";")
    # print(df)
    
    # for line in lines:
    #     print(line[9:])
        

    # data = file.read_text()
    # for line in (data):
    #     print(line)
  