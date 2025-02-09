import unittest
from heuristics import Heuristics, Node


class TestEightPuzzle(unittest.TestCase):
    def setUp(self):
        # Test puzzles with known solutions
        self.depth_0_puzzle = [[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 0]]

        self.depth_2_puzzle = [[1, 2, 3],
                               [4, 5, 6],
                               [0, 7, 8]]

        self.depth_4_puzzle = [[1, 2, 3],
                               [5, 0, 6],
                               [4, 7, 8]]

        self.depth_8_puzzle = [[1, 3, 6],
                               [5, 0, 2],
                               [4, 7, 8]]

        self.depth_12_puzzle = [[1, 3, 6],
                                [5, 0, 7],
                                [4, 8, 2]]

        self.depth_16_puzzle = [[1, 6, 7],
                                [5, 0, 3],
                                [4, 8, 2]]

        self.depth_20_puzzle = [[7, 1, 2],
                                [4, 8, 5],
                                [6, 3, 0]]

        self.depth_24_puzzle = [[0, 7, 2],
                                [4, 6, 1],
                                [3, 5, 8]]

        # tests if unsolvable puzzle returns no solution
        self.no_solution_puzzle = [[8, 1, 2],
                                   [0, 4, 3],
                                   [7, 6, 5]]

        self.heuristics_depth_0 = Heuristics(self.depth_0_puzzle)
        self.heuristics_depth_2 = Heuristics(self.depth_2_puzzle)
        self.heuristics_depth_4 = Heuristics(self.depth_4_puzzle)
        self.heuristics_depth_8 = Heuristics(self.depth_8_puzzle)
        self.heuristics_depth_12 = Heuristics(self.depth_12_puzzle)
        self.heuristics_depth_16 = Heuristics(self.depth_16_puzzle)
        self.heuristics_depth_20 = Heuristics(self.depth_20_puzzle)
        self.heuristics_depth_24 = Heuristics(self.depth_24_puzzle)
        self.heuristics_no_solution = Heuristics(self.no_solution_puzzle)

    def test_node_initialization(self):
        """Test Node object initialization and blank space detection"""
        node = Node(self.depth_2_puzzle, None, 0)
        self.assertEqual(node.blank_coords, [2, 0])
        self.assertEqual(node.depth, 0)
        self.assertEqual(node.parent, None)

    def test_move_tile(self):
        """Test tile movement functionality"""
        node = Node(self.depth_4_puzzle, None, 0)
        # Move tile up
        node.move_tile(0, 1)
        self.assertEqual(node.blank_coords, [0, 1])
        self.assertEqual(node.state[0][1], 0)
        self.assertEqual(node.state[1][1], 2)

    def test_misplaced_tile_heuristic(self):
        """Test misplaced tile heuristic calculation"""
        # For depth 8 puzzle
        cost = self.heuristics_depth_8.calculate_misplaced_tile(self.depth_8_puzzle)
        self.assertEqual(cost, 7)  # 3, 6, 5, 2, 4, 7, and 8 are misplaced

    def test_manhattan_distance_heuristic(self):
        """Test Manhattan distance heuristic calculation"""
        # For depth 12 puzzle
        cost = self.heuristics_depth_12.calculate_manhattan_distance(self.depth_12_puzzle)
        self.assertEqual(cost, 10)  # Sum of distances of misplaced tiles

    def test_expand_operations(self):
        """Test node expansion operations"""
        node = Node(self.depth_4_puzzle, None, 0)

        # Test expanding in all directions
        expanded = node.expand_all()
        self.assertEqual(len(expanded), 4)  # Should have 4 possible moves

        # Verify all expanded nodes are unique
        states = [str(n.state) for n in expanded]
        self.assertEqual(len(states), len(set(states)))

    def test_goal_state_detection(self):
        """Test if goal state is correctly identified"""
        goal_node = Node(self.depth_0_puzzle, None, 0)
        self.assertEqual(goal_node.state, Heuristics.goal_state)

    def test_invalid_moves(self):
        """Test handling of invalid moves"""
        node = Node(self.depth_8_puzzle, None, 0)
        original_state = [row[:] for row in node.state]

        # Try invalid move
        node.move_tile(2, 2)
        self.assertEqual(node.state, original_state)

    def test_depth_0_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 0 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_0.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 0)  # Should solve in 0 moves

    def test_depth_0_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 0 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_0.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 0)  # Should solve in 0 moves

    def test_depth_0_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 0 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_0.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 0)  # Should solve in 0 moves

    def test_depth_2_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 2 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_2.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 2)  # Should solve in 2 moves

    def test_depth_2_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 2 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_2.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 2)  # Should solve in 2 moves

    def test_depth_2_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 2 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_2.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 2)  # Should solve in 2 moves

    def test_depth_4_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 4 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_4.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 4)  # Should solve in 4 moves

    def test_depth_4_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 4 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_4.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 4)  # Should solve in 4 moves

    def test_depth_4_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 4 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_4.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 4)  # Should solve in 4 moves

    def test_depth_8_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 8 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_8.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 8)  # Should solve in 8 moves

    def test_depth_8_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 8 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_8.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 8)  # Should solve in 8 moves

    def test_depth_8_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 8 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_8.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 8)  # Should solve in 8 moves

    def test_depth_12_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 12 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_12.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 12)  # Should solve in 12 moves

    def test_depth_12_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 12 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_12.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 12)  # Should solve in 12 moves

    def test_depth_12_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 12 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_12.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 12)  # Should solve in 12 moves

    def test_depth_16_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 16 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_16.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 16)  # Should solve in 16 moves

    def test_depth_16_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 16 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_16.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 16)  # Should solve in 16 moves

    def test_depth_16_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 16 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_16.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 16)  # Should solve in 16 moves

    def test_depth_20_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 20 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_20.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 20)  # Should solve in 20 moves

    def test_depth_20_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 20 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_20.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 20)  # Should solve in 20 moves

    def test_depth_20_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 20 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_20.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 20)  # Should solve in 20 moves

    def test_depth_24_search_ucs(self):
        # Test if solution paths meet expected lengths
        # Test with depth 24 puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_depth_24.uniform_cost_search()
        self.assertIsNotNone(uniform_cost_search_result)
        self.assertEqual(uniform_cost_search_result.state, Heuristics.goal_state)
        self.assertEqual(uniform_cost_search_result.depth, 24)  # Should solve in 24 moves

    def test_depth_24_search_misplaced(self):
        # Test if solution paths meet expected lengths
        # Test with depth 24 puzzle
        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_depth_24.a_star_misplaced_tile()
        self.assertIsNotNone(misplaced_tile_result)
        self.assertEqual(misplaced_tile_result.state, Heuristics.goal_state)
        self.assertEqual(misplaced_tile_result.depth, 24)  # Should solve in 24 moves

    def test_depth_24_search_manhattan(self):
        # Test if solution paths meet expected lengths
        # Test with depth 24 puzzle
        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_depth_24.a_star_manhattan_distance()
        self.assertIsNotNone(manhattan_distance_result)
        self.assertEqual(manhattan_distance_result.state, Heuristics.goal_state)
        self.assertEqual(manhattan_distance_result.depth, 24)  # Should solve in 24 moves

    def test_no_solution_search(self):
        """Test if there is no solution returned"""
        # Test with unsolvable puzzle
        # Test uniform cost search
        uniform_cost_search_result = self.heuristics_no_solution.uniform_cost_search()
        self.assertIsNone(uniform_cost_search_result)   # Should not solve

        # Test A* search with misplaced tile heuristic
        misplaced_tile_result = self.heuristics_no_solution.a_star_misplaced_tile()
        self.assertIsNone(misplaced_tile_result)    # Should not solve

        # Test A* search with manhattan distance heuristic
        manhattan_distance_result = self.heuristics_no_solution.a_star_manhattan_distance()
        self.assertIsNone(manhattan_distance_result)    # Should not solve