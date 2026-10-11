# Учебная версия: выполните три TODO и проверяйте их через practice_checks.py.
import random
from support import inside, neighbours, finish
TITLE = 'Battleship'
INPUT_HELP = 'Enter row column (1–10). Fleet: 4 singles, 3 doubles, 2 triples, 1 quadruple. Ships cannot touch, even diagonally.'
LENGTHS = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)

# Корабли размещаются без касания даже по диагонали.
def generate_fleet(seed=None):
    rng = random.Random(seed)
    for _ in range(200):
        fleet = []
        occupied = set()
        for length in LENGTHS:
            candidates = []
            for r in range(10):
                for c in range(10):
                    for dr, dc in ((0, 1), (1, 0)):
                        ship = {(r + i * dr, c + i * dc) for i in range(length)}
                        if not all((inside(cell, 10, 10) for cell in ship)):
                            continue
                        halo = set(ship)
                        for cell in ship:
                            halo.update(neighbours(cell, 10, 10, True))
                        if not halo & occupied:
                            candidates.append(ship)
            if not candidates:
                break
            ship = rng.choice(candidates)
            fleet.append(ship)
            occupied.update(ship)
        if len(fleet) == 10:
            return fleet
    raise RuntimeError('Could not place fleet; restart with another seed.')

def new_game(seed=None):
    return {'fleet': generate_fleet(seed), 'shots': set(), 'finished': False, 'result': ''}

def validate_shot(state, cell):
    if cell not in state['shots'] and inside(cell, 10, 10)==True:
        return(True,'OK')
    if cell in state['shots']:
        return(False,'Already Shot')
    return (False,'Out of bounds')


def record_and_classify_shot(state, cell):
    state['shots'].add(cell)
    for ship in state['fleet']:
        if cell in ship:
            if ship <= state['shots']:
                return 'Sunk.'
            return 'Hit.'

    return 'Miss.'

def resolve_after_shot(state):
    if all(ship <= state['shots'] for ship in state['fleet']):
        return finish(state,(str(len(state['shots'])) + ' 1 shots'))
    return ''

def apply_move(state, cell):
    if state['finished']:
        return (False, 'Game finished.')
    ok, message = validate_shot(state, cell)
    if not ok:
        return (False, message)
    classification = record_and_classify_shot(state, cell)
    final = resolve_after_shot(state)
    return (True, final or classification)
