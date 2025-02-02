from typing import List
from copy import deepcopy
import heapq

class Node:
    def __init__(self, state: List[List[int]], parent, depth):
        # current state of the node
        self.state = state
        # parent of current node
        self.parent = parent
        # depth of node: g(n)
        self.depth = depth
        # heuristic cost of current node: h(n)
        self.heuristic_cost = 0

        # coords of blank stored as [row, column] starting from index 0
        self.blank_coords = []
        # automatically finds coords of blank space on object initialization
        for i in range(0, 3):
            if self.state[i].count(0) != 0:
                self.blank_coords.append(i)
                self.blank_coords.append(self.state[i].index(0))
                break

    # overriding __lt__ to allow heapq to pop the node with the lowest heuristic cost
    def __lt__(self, other):
        # For heapq comparison - compares f(n) = g(n) + h(n)
        return (self.depth + self.heuristic_cost) < (other.depth + other.heuristic_cost)

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

    # expands all possible nodes
    def expand_all(self):
        # expand nodes in all directions
        nodes = [self.expand_left(), self.expand_right(), self.expand_up(), self.expand_down()]
        # filter out null nodes where node can't be expanded in that direction
        return [node for node in nodes if node]


class Heuristics:
    def __init__(self, initial_state: List[List[int]]):
        self.initial_state = initial_state

        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]]

    def calculate_misplaced_tile(self, state: List[List[int]]) -> int:
        misplaced_tile_heuristic = 0
        # loop through each tile in state
        for i in range(0, 3):
            for j in range(0, 3):
                # increment misplaced_tile_heuristic for every tile not equal to goal_state
                if state[i][j] != 0 and (state[i][j] != self.goal_state[i][j]):
                    misplaced_tile_heuristic += 1
        return misplaced_tile_heuristic

    def calculate_manhattan_distance(self, state: List[List[int]]) -> int:
        manhattan_distance_heuristic = 0
        # loop through each tile in state
        for i in range(0, 3):
            for j in range(0, 3):
                # if tile isn't equal to goal_state, find distance
                tile = state[i][j]
                if tile != 0 and (tile != self.goal_state[i][j]):
                    # find where tile should be
                    goal_coords = [(tile - 1) // 3, (tile - 1) % 3]
                    # add the distance to manhattan_distance_heuristic
                    manhattan_distance_heuristic += abs(i - goal_coords[0]) + abs(j - goal_coords[1])

        return manhattan_distance_heuristic

    '''
    function general-search(problem, QUEUEING-FUNCTION)
        nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
        loop do
            if EMPTY(nodes)
                then return "failure" (we have proved there is no solution!)
            node = REMOVE-FRONT(nodes)
            if problem.GOAL-TEST(node.STATE) succeeds
                then return node
            nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
        end
    '''

    def a_star_search(self, heuristic_function):
        # create the root node with the initial state
        initial_node = Node(deepcopy(self.initial_state), None, 0)
        # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
        frontier_nodes = [initial_node]
        # convert frontier_nodes into a heap
        heapq.heapify(frontier_nodes)
        # keep track of visited nodes
        visited = set()
        # counter for number of nodes expanded
        nodes_expanded = 0
        # keep track of maximum size of queue
        max_queue_size = 0

        while True:
            # keep the max queue size stored
            max_queue_size = max(max_queue_size, len(frontier_nodes))

            if len(frontier_nodes) == 0:
                print("no solution")
            # node = REMOVE-FRONT(nodes)
            node = heapq.heappop(frontier_nodes)
            # if problem.GOAL - TEST(node.STATE) succeeds
            if node.state == self.goal_state:
                # goal state reached
                print(f"Depth of solution: {node.depth}")
                print(f"Number of nodes expanded: {nodes_expanded}")
                print(f"Maximum queue size: {max_queue_size}")
                return node

            # convert state to tuple for hashing
            state_tuple = tuple(map(tuple, node.state))
            # check if state is already visited
            if state_tuple in visited:
                continue

            # add the tuple to visited set
            visited.add(state_tuple)

            # nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
            expanded_nodes = node.expand_all()
            # increment the number of nodes expanded
            nodes_expanded += 1
            for expanded_node in expanded_nodes:
                # check if the child is already visited
                child_tuple = tuple(map(tuple, expanded_node.state))
                if child_tuple not in visited:
                    expanded_node.heuristic_cost = heuristic_function(expanded_node.state)
                    heapq.heappush(frontier_nodes, expanded_node)


    def uniform_cost_search(self):
        # TODO implement this
        print("\nUniform Cost Search")
        return self.a_star_search(lambda _: 0)

    def a_star_misplaced_tile(self):
        # TODO implement this
        print("\nA* with misplaced tile heuristic")
        return self.a_star_search(self.calculate_misplaced_tile)

    def a_star_manhattan_distance(self):
        # TODO implement this
        print("\nA* with manhattan distance heuristic")
        return self.a_star_search(self.calculate_manhattan_distance)