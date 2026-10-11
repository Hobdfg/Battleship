def inside(cell, rows, cols):
    return isinstance(cell, tuple) and len(cell) == 2 and all((type(x) is int for x in cell)) and (0 <= cell[0] < rows) and (0 <= cell[1] < cols)

def neighbours(cell, rows, cols, diagonal=False):
    r, c = cell
    offsets = ((-1, 0), (0, -1), (0, 1), (1, 0))
    if diagonal:
        offsets = tuple(((dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc))
    return [(r + dr, c + dc) for dr, dc in offsets if inside((r + dr, c + dc), rows, cols)]

def finish(state, result):
    state['finished'] = True
    state['result'] = result
