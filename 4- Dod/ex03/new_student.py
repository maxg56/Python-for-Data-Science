import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    first_name: str
    last_name: str
    age: int
    id: str = field(default_factory=generate_id)
    is_alive: bool = True

    def die(self):
        """Mark the student as not alive."""
        self.is_alive = False
