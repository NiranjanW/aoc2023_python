from pathlib import Path
import re


def diff(data):
    ans =[]
    for i in range(len(data)-1):
        ans.append(data[i+1] -data[i])
    return ans
def extrapolate(hist):
    layers=[hist]

    while not all( [ x ==0 for x in layers[-1]]):
        layers.append(diff(layers[-1]))
                  


if __name__ == "__main__":
    data = Path(__file__).with_name("example.txt").read_text().splitlines()
    data = (list(map(int , data[0].split())))
    ans = []
    res = [ x-y for x,y in zip(data[1:], data)]

    for i in range(len(data)-1):
        ans.append(data[i+1] -data[i])    
    print(ans)

    # print(data[0])
    # [ print(int(i) )for i in data[0] if i != ' ']
