from pathlib import Path

from Client0 import *
from Seq1 import *

print("-----| Practice 2, Exercise 6 |------")

file = "./sequences/FRAT1.txt"

IP = "212.128.255.93"
c1 = Client(IP,8080)
c2 = Client(IP,8081)

file = Path(file).read_text().split("\n")
l = len(file)
line = 1
seq1 = ""
while line < l:
    seq1 += file[line]
    line += 1
seq1 = Seq(seq1)

print("Gene FRAT1 :" + str(seq1))

b = 0
frag = (10,10) #(fragment length, Nº of fragments)
send = str(seq1)
while b < frag[1]:
    msg = send[b*frag[0]:(b+1)*frag[0]]
    print(f"Fragment {b + 1} : {msg}")
    if b % 2 == 1:
        c1.talk(msg)
    else:
        c2.talk(msg)
    b += 1
