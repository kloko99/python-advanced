import pickle
from pathlib import Path


class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("HIER WIRD CODE ausgeführt ")


members = [Member("Michi", 32), Member("Alice", 43), Member("Bob", 43)]
print(pickle.dumps(members))


with open(Path(__file__).parent / "pickel_members.pk", mode="wb") as f:
    pickle.dump(members, f)
