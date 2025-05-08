import pickle
from pathlib import Path

# hier müsste die Klasse Member importiert werden ...

with open(Path(__file__).parent / "pickel_members.pk", mode="rb") as f:
    code = pickle.load(f)

print(code)
