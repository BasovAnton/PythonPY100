EMPTY_CELL = "-"

def get_first_player():

def init_field(size=3):
    field = [
        [EMPTY_CELL for _ in range(size)]
        for _ in range(size)
    ]
    return  field

def is_win(field) -> bool:
    win_conditions = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]
    for win_comb in win_conditions:
        row_index = win_comb[0][0]
        col_index = win_comb[0][1]
        cell_1 = field[win_comb[0][0]]

def is_available_ceil(field) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return  True
    return False

def is_empty_cell(field: list, x: int, y: int) -> bool:
    cell = field[x][y]
    if cell == EMPTY_CELL:
        return True
    else:
        return False