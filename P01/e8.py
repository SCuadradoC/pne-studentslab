from Seq1 import *

s1 = Seq()
s2 = Seq("TAGAC")
s3 = Seq("Invalid sequence")
print("")

n = 0
for e in [s1,s2,s3]:
    n += 1
    print(f"""Sequence {n} (Length: {e.len()}): {e}
Bases: {e.count()}
Rev: {e.reverse()}
Comp: {e.complement()}
""")