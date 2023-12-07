
from pathlib import Path 
import os


if __name__ == '__main__':
    input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
reb7uchetzz
    """
    # full_path = os.fspath(Path(__file__).parent/'data/')
    # print(full_path)
    file_path = (str(Path.cwd())+"/day1/data/"+"input.txt")
    file = Path(file_path)
    data = file.read_text().strip()
    # print(data)

    # first = [  (i[:1]) for i in input.strip().split('\n')]
    # last = [  (i[-1:]) for i in input.strip().split('\n')]
    # first += last
    # print(f" {first} += {last}")
    # first = [ print((j)) for i in input.split('\n') for j in i.strip() ]

    ans = 0
    for line in data.split('\n'):
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        score = int(digits[0] + digits[-1])
        
        ans += score
    print(ans)

    def num_sum(data) :
        ans =0 
        for line in data.split('\n'):
            digits = []
            for chr in line:
                if chr.isdigit():
                    digits.append(chr)
            for i ,val in enumerate( 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine'):
                if val in line[1:]:
                    digits.append(i)
 




    
    