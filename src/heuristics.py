from typing import List
from copy import deepcopy

class Node:
    def __init__(self, state: List[List[int]], parent, depth):
        # current state of the node
        self.state = state
        # parent of current node
        self.parent = parent
        # depth of node
        self.depth = depth

        # coords of blank stored as [row, column] starting from index 0
        self.blank_coords = []
        # automatically finds coords of blank space on object initialization
        for i in range(0, 3):
            if self.state[i].count(0) != 0:
                self.blank_coords.append(i)
                self.blank_coords.append(self.state[i].index(0))
                break

    # function for moving a single tile
    def move_tile(self, row, col):
        # first check if given coords are next to blank (0)
        # either same row and 1 away from col or same col and 1 away from row
        if ((row == self.blank_coords[0] and abs(col - self.blank_coords[1]) == 1)
                or (col == self.blank_coords[1] and abs(row - self.blank_coords[0]) == 1)):
            # swap given tile and blank
            self.state[self.blank_coords[0]][self.blank_coords[1]] = self.state[row][col]
            self.state[row][col] = 0
            # set blank coords to new coords
            self.blank_coords = [row, col]
        else:
            print("Invalid move")

        return 0

    def print_state(self):
        for i in range(0, 3):
            print(self.state[i])

    # expands the node where the blank is moved to the left
    def expand_left(self):
        # first check if possible
        if self.blank_coords[1] > 0:
            # create a new child node, copying the parent state
            left_child = Node(deepcopy(self.state), self, self.depth + 1)
            # move the blank to the left
            left_child.move_tile(self.blank_coords[0], self.blank_coords[1] - 1)

            return left_child

        return None

    # expands the node where the blank is moved to the right
    def expand_right(self):
        # first check if possible
        if self.blank_coords[1] < 2:
            # create a new child node, copying the parent state
            right_child = Node(deepcopy(self.state), self, self.depth + 1)
            # move the blank to the right
            right_child.move_tile(self.blank_coords[0], self.blank_coords[1] + 1)

            return right_child

        return None

    # expands the node where the blank is moved up
    def expand_up(self):
        # first check if possible
        if self.blank_coords[0] > 0:
            # create a new child node, copying the parent state
            up_child = Node(deepcopy(self.state), self, self.depth + 1)
            # move the blank up
            up_child.move_tile(self.blank_coords[0] - 1, self.blank_coords[1])

            return up_child

        return None

    # expands the node where the blank is moved down
    def expand_down(self):
        # first check if possible
        if self.blank_coords[0] < 2:
            # create a new child node, copying the parent state
            down_child = Node(deepcopy(self.state), self, self.depth + 1)
            # move the blank down
            down_child.move_tile(self.blank_coords[0] + 1, self.blank_coords[1])

            return down_child

        return None


class Heuristics:
    def __init__(self, initial_state: List[List[int]]):
        self.initial_state = initial_state

        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]]

    def uniform_cost_search(self):
        # TODO implement this
        return 0

    def a_star_misplaced_tile(self):
        # TODO implement this
        return 0

    def a_star_manhattan_distance(self):
        # TODO implement this
        return 0
