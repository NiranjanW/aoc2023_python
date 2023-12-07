from pathlib import Path
import re
class Function() :

    def __init__(self ,s) -> None:
        data = s.split('\n')[1:]
        self.tuples : list[tuple[int, int,int]] = [ [ int(x) for x in line.split()] for line in data]

    def apply_one(self , x:int) -> int :
        for (dst,src,sz) in self.tuples:
            if  src<=x<src+sz:
                return x+dst-src
                
        return x
    
    def apply_range (self,R):
        pass


if __name__ == "__main__":

    filepath = str(Path.cwd()) + "/day5/data/example.txt"
    file_hand = Path(filepath)
    data = open(file_hand).read().strip()
    # L = data.split('\n')
    # print(L)
    parts = data.split('\n\n')
    # print(parts)
    seed , *other = parts
    seed = [int(x) for x in seed.split(':')[1].split()]
    #print(seed)
    Fs = [ Function(x) for x in other]
    # P1= []
    # for s in seed:
    #     for f in Fs:
    #         s = (f.apply_one(s))
    #     P1.append(s)
    # # print((P1))
    # print(min(P1))

    pairs = list(zip(seed[::2] ,seed[1::2]))
    print(pairs)

    for st , en in pairs:
        R = [(st ,st +en)]
    
        for f in Fs:
            R = f.apply_range(R)
    
    # print (data)
    # for line in data:
    #     print(line)
    #     parts = re.split("\s+", line)
    #     print(parts[1:])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    # seeds * other = 