from datetime import datetime


class Fruit:
    id: int
    name: str
    created_at: int
    updated_at: int

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def udpate(self, name: str) -> str:
        old_name = self.name
        self.name = name
        self.updated_at = datetime.now()

        return old_name
