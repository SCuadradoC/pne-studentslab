from Seq0 import *
from Seq1 import *

s1 = dna_seq()
s2 = dna_seq()



seq1 = "ATTCCCGGGG"

print(f"Seq:    {seq1}")
print(f"  Rev : {seq_reverse(seq1)}")
print(f"  Comp: {seq_complement(seq1)}")
print(f"  Length: {seq_len(seq1)}")
print(f"    A: {seq_count_base(seq1)['A']}")
print(f"    T: {seq_count_base(seq1)['T']}")
print(f"    C: {seq_count_base(seq1)['C']}")
print(f"    G: {seq_count_base(seq1)['G']}")



s1 = dna_seq("AGTACACTGGT")
s2 = dna_seq("CGTAAC")
g = Gene("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")
