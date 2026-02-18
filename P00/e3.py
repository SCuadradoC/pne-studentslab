import Seq0
path = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN"]
filetype = ".txt"

for e in filenames:
    print("Gene " + e + " -> Length: " + str(Seq0.seq_len(path + e + filetype)))
