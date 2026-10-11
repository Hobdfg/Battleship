import game

def print_grid(board):
    width = max(2, max((len(str(v)) for row in board for v in row)))
    print(' ' * (width + 1) + ' '.join((str(c + 1).rjust(width) for c in range(len(board[0])))))
    for r, row in enumerate(board):
        print(str(r + 1).rjust(width) + ' ' + ' '.join((str(v).rjust(width) for v in row)))

def parse_move(raw):
    parts = raw.split()
    if len(parts) != 2:
        raise ValueError('Enter row column.')
    return tuple((int(x) - 1 for x in parts))

def render(state):
    occupied = set().union(*state['fleet'])
    print_grid([['X' if (r, c) in occupied else 'o' if (r, c) in state['shots'] else '.' for c in range(10)] for r in range(10)] if state['finished'] else [['X' if (r, c) in state['shots'] and (r, c) in occupied else 'o' if (r, c) in state['shots'] else '.' for c in range(10)] for r in range(10)])
    print('Shots:', len(state['shots']), '| Sunk:', sum((ship <= state['shots'] for ship in state['fleet'])), '/ 10')

def run(seed=None):
    state = game.new_game(seed)
    print(game.TITLE)
    print(game.INPUT_HELP)
    print('Learning loop / Учебный цикл: run → fix the next TODO in game.py → rerun.')
    print('Commands: help | restart | quit')
    while True:
        render(state)
        if state['finished']:
            print(state['result'])
            return state
        try:
            raw = input('Move> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nSession ended.')
            return state
        if raw.lower() in ('q', 'quit', 'exit'):
            return state
        if raw.lower() == 'help':
            print(game.INPUT_HELP)
            print('Open game.py and work only on TODO 1 → TODO 2 → TODO 3. / Откройте game.py и выполняйте только TODO 1 → TODO 2 → TODO 3.')
            continue
        if raw.lower() == 'restart':
            state = game.new_game(seed)
            continue
        try:
            move = parse_move(raw)
        except ValueError as error:
            print('Invalid input:', error)
            continue
        try:
            accepted, message = game.apply_move(state, move)
        except NotImplementedError as error:
            print('\nNEXT / СЛЕДУЮЩИЙ ШАГ:')
            print(error)
            print('Implement only that TODO, run practice_checks.py, then rerun main.py. / Реализуйте только этот TODO, запустите practice_checks.py и снова main.py.')
            return state
        print(('OK: ' if accepted else 'Rejected: ') + message)
