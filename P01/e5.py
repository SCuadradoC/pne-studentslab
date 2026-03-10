from Seq1 import *

s1 = Seq()
s2 = Seq("TAGAC")
s3 = Seq("Invalid sequence")


print(f"Sequence 3 (Length: {s1.len()}): {s1}")
s1.count_base()
print(f"Sequence 3 (Length: {s2.len()}): {s2}")
s2.count_base()
print(f"Sequence 3 (Length: {s3.len()}): {s3}")
s3.count_base()
