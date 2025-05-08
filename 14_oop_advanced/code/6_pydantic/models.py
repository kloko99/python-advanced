import pydantic
from typing import Literal


class Wizard(pydantic.BaseModel):
    """Pydantic Klasse, die von pydantic validiert wird."""

    id: pydantic.PositiveInt
    name: str
    age: int
    intelligence: pydantic.StrictInt
    power: pydantic.PositiveInt
    type: Literal["wizard", "witcher"]
    origin: str | None = None
    history: list[int | None]
    magic: int
    superPower: bool
    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        extra="forbid",  # Objekt kann nachtäglich keine weiteren Attribute haben
    )
