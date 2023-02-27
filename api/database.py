from api.models import Fruit


class IdGenerator:
    inner: int

    def __init__(self, starting_id: int):
        self.inner = starting_id

    def next(self) -> int:
        id = self.inner
        self.inner += 1

        return id


database = {
    "fruit":  {
        0: Fruit(0, "apple"),
        1: Fruit(1, "kiwi"),
        2: Fruit(2, "strawberry"),
    }
}
