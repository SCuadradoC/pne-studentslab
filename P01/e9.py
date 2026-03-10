from Seq1 import *

s1 = Seq()
s1.read_fasta("./U5.txt")

print(f"""Sequence (Length: {s1.len()}): {s1}
Bases: {s1.count()}
Rev: {s1.reverse()}
Comp: {s1.complement()}
""")