from pathlib import Path
import json

genes = json.loads(Path("./P07/genes.json").read_text())
print(genes)
