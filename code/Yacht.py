from code.Ship import Ship


class Yacht(Ship):
    def __init__(self, image, start_position: tuple[int, int]):
        super().__init__(image, start_position)
