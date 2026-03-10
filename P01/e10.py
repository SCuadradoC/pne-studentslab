from Seq1 import *

PATH = "./"
names = ["ADA","FRAT1","FXN","RNU6_269P","U5"]
FILETYPE = ".txt"
Seqs = []

for e in names:
    s = Seq()
    s.read_fasta(PATH + e + FILETYPE)
    freqs = s.count()
    f = ["",0]
    for b in freqs:
        if freqs[b] > f[1]:
            f[0] = b
            f[1] = freqs[b]
    print(f"Gene {e}: Most frequent Base: {f[0]} \n")
