from pathlib import Path

print(len(Path("sequences/ADA.txt").read_text()))
lines = Path("sequences/ADA.txt").read_text().split("\n")
l = len(lines)
t = 1
base_num = 0
while t < l:
    base_num += len(lines[t])
    t += 1
print(base_num)
