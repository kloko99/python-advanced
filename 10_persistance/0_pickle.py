"""
Pickle: Daten in Bytestream serialisieren
"""

import pickle
import json

# Ein Set erstellen
data = set([1, 2, 3, 4])


# json_data = json.dumps(data)  # object of type set is not JSON serializable

# nach Pickle umwandeln (Bytes)
pickled_data = pickle.dumps(data)
print(pickled_data, type(pickled_data))

# nach Python umwandeln
python_data = pickle.loads(pickled_data)
print(python_data, type(python_data))
