"""
 * wir wollen diese finite state machine programmieren
 *https://en.wikipedia.org/wiki/Finite-state_machine#/media/File:Turnstile_state_machine_colored.svg

Wenn wir im Zustand "locked" sind prüfen wir den Event"
Wenn wir im Zusstasnd "unlocked" sind prüfen wir den Event
wir gehen von einem Zustand in einen nächsten Zustand (dieser
kann auch der gleiche sein.)
"""
from enum import Enum, auto


class State(Enum):
    """Zustände des Drehkreuzes."""
    locked = auto()
    unlocked = auto()


class Event(Enum):
    """Aktionen, die am Drehkreuz durchgeführt werden können."""
    push = auto()
    insert = auto()


def next_state(state: State, event: Event) -> State:
    """Hole den nächsten Zustand auf Basis von Zustand und Aktion."""
    match state:
        case State.locked:
            match event:
                case Event.push:
                    state = State.locked
                case Event.insert:
                    state = State.unlocked
        case State.unlocked:
            match event:
                case Event.push:
                    state = State.locked
                case Event.insert:
                    state = State.unlocked
    return state


if __name__ == "__main__":
    # gegen geschlossenes Drehkreuz drücken
    initial_state = State.locked
    state = next_state(initial_state, Event.push)
    print(state) # State.locked

    # geschlossenes Drehkreuz und Geld reinschmeissen
    initial_state = State.locked
    state = next_state(initial_state, Event.insert)
    print(state) # State.unlocked
