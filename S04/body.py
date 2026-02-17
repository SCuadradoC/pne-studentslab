from pathlib import Path

lines = Path("sequences/U5.txt").read_text().split("\n")
l = len(lines)
t = 1
seq = ""
while t < l:
    seq = seq + lines[t]
    t += 1
print(seq)
