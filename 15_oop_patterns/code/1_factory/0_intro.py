"""
The Factory Pattern is a creational design pattern that provides an interface
for creating objects in a super factory method but allows subclasses to alter
the type of objects that will be created. In Python, you can implement the
Factory Pattern using class methods or functions.
methods:

"""

from typing import Protocol


class VehicleDoesNotExist(Exception):
    """Eigene Fehlerklasse für fehlende Fahrzeuge."""

    pass


class Vehicle(Protocol):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} {self.model} car's engine started"


class MotorCycle(Vehicle):
    def start_engine(self):
        return f"{self.brand} {self.model} motorcycle engine started"


def vehicle_factory(vehicle_type, brand, model) -> Vehicle:
    """Vehicle Fabrik erstellt in Abhängikeit von vecicle_type
    die entsprechende Klasse."""
    if vehicle_type.lower() == "car":
        return Car(brand=brand, model=model)
    if vehicle_type.lower() == "motorcycle":
        return MotorCycle(brand=brand, model=model)

    raise VehicleDoesNotExist(f"Dieses Fahrzeug existiert nicht: {vehicle_type}")


bmw_object = vehicle_factory("Car", "BMW", "Z34")
fahrzeuge = ["Car, BMW, Z34", "Motorcycle, Toyota, U34"]

for fahrzeug_string in fahrzeuge:
    obj = vehicle_factory(*fahrzeug_string.split(","))
    print(obj)
