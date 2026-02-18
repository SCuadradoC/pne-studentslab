import Seq0
path = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN"]
filetype = ".txt"

for e in filenames:
    mesg = "Gene " + e + ":\n"
    bases = Seq0.seq_count_base(path + e + filetype)
    for b in bases:
        mesg += "   " + b + ": " + str(bases[b]) + "\n"
    mesg += "\n"
    print(mesg)
