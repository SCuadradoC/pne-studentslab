import Seq1

path = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN"]
filetype = ".txt"


print("-----| Exercise 8 |------")

for e in filenames:
    freqs = Seq1.seq_count_base(path + e + filetype)
    #print(freqs)
    #break
    out = ["",0]
    for b in freqs:
        if freqs[b] > out[1]:
            out = [b,freqs[b]]
    print("Gene " + e + ": Most frequent base: " + out[0])
