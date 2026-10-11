import unittest
from copy import deepcopy
import game
from console import parse_move

class BaseGameTests(unittest.TestCase):

    def rejected(self, state, move):
        before = deepcopy(state)
        self.assertFalse(game.apply_move(state, move)[0])
        self.assertEqual(state, before, 'Rejected move must not change state.')

    def test_fleet_and_shots(self):
        for seed in range(5):
            s = game.new_game(seed)
            self.assertEqual(sorted(map(len, s['fleet'])), [1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
            self.assertEqual(len(set().union(*s['fleet'])), 20)
            for i, a in enumerate(s['fleet']):
                for b in s['fleet'][i + 1:]:
                    self.assertTrue(all((max(abs(x[0] - y[0]), abs(x[1] - y[1])) > 1 for x in a for y in b)))
        self.rejected(s, (-1, 0))
        cell = next(iter(s['fleet'][0]))
        game.apply_move(s, cell)
        self.rejected(s, cell)
        for cell in sorted(set().union(*s['fleet'])):
            if cell not in s['shots']:
                game.apply_move(s, cell)
        self.assertTrue(s['finished'])
        self.rejected(s, (0, 0))
if __name__ == '__main__':
    unittest.main(verbosity=2)
