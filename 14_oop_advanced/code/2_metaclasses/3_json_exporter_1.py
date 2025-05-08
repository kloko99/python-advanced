"""
Wie kann in der abgeleiteten Klasses des JsonExporters die
sichergestellt werden, dass _filename ein String ist und mit .json endet?
"""

import pathlib
import json

BASE_DIR = pathlib.Path(__file__).parent


class JsonExporter:
    def __init__(self, raw_data_list):
        self.raw_data = raw_data_list

    def export(self):
        with open(BASE_DIR / self._filename, "w") as f:
            data = self._build_from_raw_data()
            json.dump(data, f)

    def _build_from_raw_data(self):
        pass


class InvoicesExporter(JsonExporter):
    pass


i = InvoicesExporter(
    [
        ["2343XE242343", 50],
        ["234X233222", 100],
        ["234299P999", 120],
        ["AC4233222", 800],
    ]
)
i.export()
