from Seq1 import Seq


s1 = Seq()
s2 = Seq("TAGAC")
s3 = Seq("Invalid(?)")

print(f"Sequence 1 (Length: {s1.len()}): {s1}")
print(f"Sequence 2 (Length: {s2.len()}): {s2}")
print(f"Sequence 3 (Length: {s3.len()}): {s3}")