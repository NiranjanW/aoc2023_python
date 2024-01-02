from  pathlib import Path
lines = Path(__file__).with_name("example.txt").read_text().strip().split(',')
print(lines)
s = [line for line in lines]
# print(s)
def HASH(s):
     value= 0
     for chr in s:
          
          value += ord(chr)
          value *= 17
          value %=256
          
     return value

cur =0
ans =0
for str in lines:
  cur = HASH(str)
  ans += cur
print(ans)

boxes = [[] for i in range(256)]


for str in lines:
    if "=" in str:
        label = str[:str.index("=")]
        box = HASH(label)
        focal_len = int(str[str.index("=")+1:])
        lens = list(filter(lambda x:x[0] == label , boxes[box]))

        if len(lens) >0 :
            idx = boxes[box].index(lens[0])
            boxes[box][idx] = [label, focal_len]
        else:
            boxes[box].append([label, focal_len])



    if "-" in str:
        label =str[:str.index("-")]
        box = HASH(label)
        lens = list(filter(lambda x: x[0] == label, boxes[box]))
        if len(lens) > 0:
            idx = boxes[box].index(lens[0])
            boxes[box].pop(idx)
ans = 0

for i, box in enumerate(boxes):
    power = 0
    for j, lens in enumerate(box):
        power += (1 + i) * (j + 1) * lens[1]

    ans += power

print(ans)

# with open("/Users/itnxw/aoc2023_python/day15/input.txt") as fin:
#     line = fin.read().strip()


# def HASH(s):
#     cur = 0
#     for c in s:
#         cur += ord(c)
#         cur *= 17
#         cur %= 256
#     return cur


# parts = line.split(",")
# cur = 0
# ans = 0
# for part in parts:
#     cur = HASH(part)
#     ans += cur

# print(ans)