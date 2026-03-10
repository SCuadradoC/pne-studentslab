import Seq1

path = "./S04/sequences/"
filenames = ["U5", "ADA", "FRAT1", "FXN"]
filetype = ".txt"

print("""------| Exercise 7 |------
Gene U5""")
seq = Seq1.seq_read_fasta(path + filenames[0] + filetype)[0:20]
print("Fragment: " + seq)
print("Complementary: " + Seq1.seq_complementary(seq))

