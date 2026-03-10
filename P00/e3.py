import Seq1
path = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN"]
filetype = ".txt"

print("-----| Exercise 3 |------")
for e in filenames:
    print("Gene " + e + " -> Length: " + str(Seq1.seq_len(path + e + filetype)))
