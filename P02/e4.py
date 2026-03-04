from Client0 import *
from Seq1 import *

PATH = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN","RNU6_269P"]
FILETYPE = ".txt"

c1 = Client("212.128.255.93",8080)


for e in filenames:
    r