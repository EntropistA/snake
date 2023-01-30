from collections import namedtuple, deque
import random

LEFT_KEY = 105
RIGHT_KEY = 106
UP_KEY = 103
DOWN_KEY = 108

EMPTY_TILE = "_"

Position = namedtuple("Position", "row column")

SNAKE_EMOJI = "🐹"
FRUIT_EMOJI = "🌽"
EMPTY_FIELD_EMOJI = "🟫"
MARGIN_EMOJI = "🧱"

class Board:
    MIN_WIDTH = 5
    MIN_HEIGHT = 5

    def __get__(self, instance, owner):
        return self.board

    def __set__(self, instance, value):
        if not self._is_valid_board(value):
            raise ValueError("Wrong board size.")
        self.board = value

    def _is_valid_board(self, board):
        return len(board) >= self.MIN_HEIGHT and all(len(row) >= self.MIN_WIDTH for row in board)


class Game:
    board = Board()

    def __init__(self, board_length, board_width):
        self.board_length = board_length
        self.board_width = board_width
        self.board = [[EMPTY_FIELD_EMOJI] * self.board_length for _ in range(self.board_width)]

        self.snake_head_pos = None
        self.snake_pos = None

        self.fruits_pos = set()

        self.all_tiles = [Position(row, column) for column in range(self.board_length) for row in
                          range(self.board_width)]

        self.score = 0

    @property
    def free_tiles(self):
        return [tile for tile in self.all_tiles if tile not in self.snake_pos and tile not in self.fruits_pos]

    def new_food_position(self) -> Position:
        return random.choice(self.free_tiles)

    def spawn_food(self) -> None:
        row, column = self.new_food_position()
        self.board[row][column] = FRUIT_EMOJI

    def spawn_snake(self):
        self.snake_head_pos = Position(self.board_width // 2, self.board_length // 2)
        self.snake_pos = deque([self.snake_head_pos])

        self.board[self.snake_head_pos.row][self.snake_head_pos.column] = SNAKE_EMOJI

    def render_screen(self):
        horizontal_margin = MARGIN_EMOJI * (self.board_length + 2)
        print(horizontal_margin)
        for row in self.board:
            print(MARGIN_EMOJI, end="")
            for element in row:
                print(element, end="")
            print(MARGIN_EMOJI)
        print(horizontal_margin)

    def start(self):
        self.spawn_snake()
        self.spawn_food()
        self.render_screen()


# class TestGame:
#     def test_board_creation(self):
#         game = Game(5, 10)
#         len()


if __name__ == "__main__":
    game = Game(10, 10)
    game.start()