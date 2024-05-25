from abc import ABC, abstractmethod
from pydantic import BaseModel

class Person(ABC, BaseModel):
    id: int
    name: str
    gender: str
    created_at: int

    @abstractmethod
    def do_habit(self):
        pass