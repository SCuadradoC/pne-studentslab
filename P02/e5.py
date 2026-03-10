from pathlib import Path

from Client0 import *
from Seq1 import *

print("-----| Practice 2, Exercise 5 |------")

file = "./sequences/FRAT1.txt"


c1 = Client("212.128.255.93",8080)

file = Path(file).read_text().split("\n")
l = len(file)
line = 1
seq1 = ""
while line < l:
    seq1 += file[line]
    line += 1
seq1 = Seq(seq1)


b = 0
while b < 50:
    send = str(seq1)[b:b+10]
    print(f"Fragment {int(b / 10 + 1)} : {send}")
    c1.talk(send)
    b += 10
