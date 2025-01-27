from unittest import TestCase


class Test(TestCase):
    def setUp(self) -> None:
        self.puzzle = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]]

    def test_uniform_cost_search(self):
        self.assertEqual(self.puzzle, [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]])
