import Seq0
path = "./S04/sequences/"
filename = "U5.txt"

seq = Seq0.seq_read_fasta(path + filename)

print("""DNA file: U5.txt
      The first 20 bases are: """ + seq[0:20])
