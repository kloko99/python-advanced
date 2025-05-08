import pathlib
import abc
import json

BASE_DIR = pathlib.Path(__file__).parent


class JsonExporterValidationError(Exception):
    pass


class ExporterMeta(type):
    subclass_filenames = set()

    def __new__(cls, classname, bases, namespace):
        pass


class JsonExporter(metaclass=ExporterMeta):
    def __init__(self, raw_data_list):
        self.raw_data = raw_data_list

    def export(self):
        with open(BASE_DIR / self._filename, "w") as f:
            data = self._build_from_raw_data()
            json.dump(data, f)

    def _build_from_raw_data(self):
        pass


class InvoicesExporter(JsonExporter):
    """
    you need to implement
    _filename
    _build from raw data
    """

    _filename = "invoices.json"

    def _build_from_raw_data(self) -> dict:
        d = []
        for entry in self.raw_data:
            uuid, price = entry
            d.append({"uuid": uuid, "price": price})
        return d


i = InvoicesExporter(
    [
        ["2343XE242343", 50],
        ["234X233222", 100],
        ["234299P999", 120],
        ["AC4233222", 800],
    ]
)
i.export()
