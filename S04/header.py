from pathlib import Path

lines = Path("sequences/RNU6_269P.txt").read_text().split("\n")
print(lines[0])
