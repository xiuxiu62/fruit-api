from copy import copy
import datetime
from typing import Optional

from api.database import IdGenerator
from api.models import Fruit


class FruitService:
    db_connection: dict[int: Fruit]
    id_generator: IdGenerator

    def __init__(self, db_connection: dict[str: dict[int: Fruit]]):
        self.db_connection = db_connection.get("fruit")
        self.id_generator = IdGenerator(3)

    def list(self) -> list[Fruit]:
        return list(self.db_connection.values())

    def get(self, id: int) -> Optional[Fruit]:
        return self.db_connection.get(id)

    def create(self, name: str):
        id = self.id_generator.next()
        self.db_connection[id] = Fruit(id, name)

    def update_or_insert(self, id: int, name: str) -> Optional[Fruit]:
        match self.db_connection.get(id):
            case None:
                self.create(name)
                return None
            case fruit:
                old_fruit = copy(fruit)
                fruit.name = name
                fruit.updated_at = datetime.now()

                return old_fruit

    def remove(self, id: int) -> Optional[Fruit]:
        fruit = self.db_connection[id]
        del self.db_connection[id]

        return fruit
