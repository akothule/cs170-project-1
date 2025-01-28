from typing import List


class Heuristics:
    def __init__(self, initial_state: List[List[int]]):
        self.initial_state = initial_state

        self.current_state = initial_state

        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]]

    def print_state(self, state: List[List[int]]):
        for i in range(0, 3):
            print(state[i])

    def uniform_cost_search(self):
        return 0

    def a_star_misplaced_tile(self):
        return 0

    def a_star_manhattan_distance(self):
        return 0
