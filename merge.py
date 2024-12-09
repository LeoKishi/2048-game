from copy import deepcopy


def merge_left(grid:list) -> bool:
    start = deepcopy(grid)

    for x in range(4):
        stack = [num for num in grid[x] if num != 0]

        for y in range(4):
            if len(stack) > 1 and stack[0] == stack[1]:
                grid[x][y] = stack.pop(0) + stack.pop(0)
            elif stack:
                grid[x][y] = stack.pop(0)
            else:
                grid[x][y] = 0

    return grid != start


def merge_right(grid:list) -> bool:
    flip(grid)
    state = merge_left(grid)
    flip(grid)
    return state


def merge_up(grid:list) -> bool:
    rotate(grid)
    state = merge_left(grid)
    rotate(grid)
    return state


def merge_down(grid:list) -> bool:
    rotate(grid)
    flip(grid)
    state = merge_left(grid)
    flip(grid)
    rotate(grid)
    return state
    

def flip(grid:list):
    for x in range(4):
        grid[x] = grid[x][::-1]


def rotate(grid:list):
    for i, row in enumerate(list(zip(*grid))):
        grid[i] = list(row)
        