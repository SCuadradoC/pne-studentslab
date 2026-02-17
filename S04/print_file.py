from pathlib import Path


FILENAME = "RNU6_269P.txt"
file_contents = Path("sequences/" + FILENAME).read_text()
print(file_contents)

