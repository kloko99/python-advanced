"""
We define an enumeration TrafficLightState to represent the states of the
traffic light: RED, YELLOW, and GREEN.

We create a TrafficLight class that has an initial state of RED.

The change_state method allows us to set the state of the traffic light to
a specific value.  The next_state method simulates the transition from one
state to the next in the sequence of RED → GREEN → YELLOW → RED.

In the client code, we create an instance of the TrafficLight class and
simulate state transitions by calling next_state() repeatedly.  

"""
from enum import Enum


class TrafficLight:
    """Class representing a traffic light.

    It can be in one of three states: RED, YELLOW, or GREEN. 
    The default state is RED.
    """

    def __init__(self):
        # self.state = ???  #set state to RED
        pass

    def next_state(self):
        """Set the state to the next state in the sequence."""
        # if state is red, set to green
        # if state is green, set to yellow
        # if state is yellow, set to red
        pass

    def __str__(self):
        return str(self.state.name)


# Client code
if __name__ == "__main__":
    traffic_light = TrafficLight()
    print("Initial state:", traffic_light)

    # Simulate traffic light changes
    for _ in range(5):
        traffic_light.next_state()
        print("Next state:", traffic_light)
