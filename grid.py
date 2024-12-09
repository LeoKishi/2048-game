from random import randint, choices
from merge import *


class Grid:
    def __init__(self):
        self.new_grid()
        self.is_paused = False


    def spawn_number(self) -> bool:
        self.find_empty_cells()

        if len(self.empty_cells) > 0:
            x, y = self.empty_cells.pop(randint(0, len(self.empty_cells)-1))
            self.grid[x][y] = choices([2,4], [0.9, 0.1]).pop()
            return True
        else:
            return False


    def merge_numbers(self, side:str) -> bool:
        match side:
            case 'Left':
                return merge_left(self.grid)

            case 'Right':
                return merge_right(self.grid)

            case 'Up':
                return merge_up(self.grid)

            case 'Down':
                return merge_down(self.grid)


    def find_empty_cells(self):
        self.empty_cells = list()

        for x in range(4):
            for y in range(4):
                if self.grid[x][y] == 0:
                    self.empty_cells.append((x,y))


    def is_stuck(self) -> bool:
        for x in range(4):
            horizontal = 0
            vertical = 0

            for y in range(4):
                if self.grid[x][y] == 0:
                    return False

                if horizontal == self.grid[x][y]:
                    return False
                else:
                    horizontal = self.grid[x][y]

                if vertical == self.grid[y][x]:
                    return False
                else:
                    vertical = self.grid[y][x]
        return True
                

    def check_milestone(self):
        for x in range(4):
            for y in range(4):
                num = self.grid[x][y]

                if num // 2048 > 0 and num not in self.milestones:
                    self.milestones.add(num)
                    print(f'{num}!')


    def new_grid(self):
        self.grid = [[0 for col in range(4)] for row in range(4)]
        self.empty_cells = [(x,y) for x in range(4) for y in range(4)]
        self.milestones = set()

        self.spawn_number()
        self.spawn_number()


    def pause(self):
        self.is_paused = True


    def unpause(self):
        self.is_paused = False
