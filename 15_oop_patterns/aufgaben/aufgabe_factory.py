"""
Create three classes: Device (abstract or protocol), Keyboard, and
Mouse, representing computer peripherals. Keyboard and Mouse inherit
from Device. Both should implement a use method that returns a string
describing usage (e.g., typing for keyboards, clicking for mice).

Implement a factory function create_peripheral(peripheral_type, brand)
that returns an instance of the chosen type. Raise ValueError if the
type is invalid.

Client code:
Prompt for peripheral type (keyboard/mouse) and brand. Use the factory
to create the peripheral, call its use method, and print the result.
"""

# Implement the Keyboard and Mouse classes here

# Implement the create_peripheral factory function here

if __name__ == "__main__":
    try:
        peripheral_type = input("Enter peripheral type (keyboard/mouse): ")
        brand = input("Enter brand: ")

        peripheral = create_peripheral(peripheral_type, brand)
        result = peripheral.use()
        print(f"{brand} {peripheral_type} is used for {result}")
    except ValueError as e:
        print(e)
