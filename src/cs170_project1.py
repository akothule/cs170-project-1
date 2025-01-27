from heuristics import Heuristics


def main():
    # take user input for initial state
    initial_state = input("Enter an initial state: ")

    heuristics = Heuristics(initial_state)

    # call all 3 algorithms
    heuristics.uniform_cost_search()
    heuristics.aStar_misplaced_tile()
    heuristics.aStar_manhattan_distance()

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # call main
    main()
