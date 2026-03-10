from pathlib import Path

from Client0 import *
from Seq1 import *

print("-----| Practice 2, Exercise 4 |------")

PATH = "./sequences/"
filenames = ["U5", "ADA", "FRAT1"]
FILETYPE = ".txt"

c1 = Client("212.128.255.93",8080)


for e in filenames:
    file = Path(PATH + e + FILETYPE).read_text().split("\n")
    l = len(file)
    line = 1
    s = ""
    while line < l:
        s += file[line]
        line += 1
    s = Seq(s)
    c1.talk(str(s))