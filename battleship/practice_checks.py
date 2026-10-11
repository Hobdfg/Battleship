import unittest
import game

class Milestones(unittest.TestCase):

    def test_1_validate(self):
        s = game.new_game(1)
        self.assertTrue(game.validate_shot(s, (0, 0))[0])
        self.assertFalse(game.validate_shot(s, (-1, 0))[0])
        s['shots'].add((0, 0))
        self.assertFalse(game.validate_shot(s, (0, 0))[0])

    def test_2_classify(self):
        s = {'fleet': [{(1, 1), (1, 2)}], 'shots': set(), 'finished': False, 'result': ''}
        self.assertEqual(game.record_and_classify_shot(s, (0, 0)), 'Miss.')
        self.assertEqual(game.record_and_classify_shot(s, (1, 1)), 'Hit.')
        self.assertEqual(game.record_and_classify_shot(s, (1, 2)), 'Sunk.')

    def test_3_resolve(self):
        s = {'fleet': [{(1, 1)}], 'shots': {(1, 1)}, 'finished': False, 'result': ''}
        game.resolve_after_shot(s)
        self.assertTrue(s['finished'])
        self.assertIn('1 shots', s['result'])
if __name__ == '__main__':
    unittest.main(verbosity=2)
