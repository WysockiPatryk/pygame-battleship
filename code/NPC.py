from code.Player import Player


class NPC(Player):
    __available_difficulty_levels = [1, 2]

    def __init__(self, difficulty_level: int):
        super().__init__('PC')
        self.__set_difficulty_level(difficulty_level)

    def __set_difficulty_level(self, difficulty_level: int):
        self.difficulty_level = difficulty_level if difficulty_level in self.__available_difficulty_levels \
            else self.__available_difficulty_levels[-1]
