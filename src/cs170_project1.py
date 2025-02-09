from heuristics import Heuristics


def main():
    while True:
        # take user input for initial state
        print("Enter a valid initial state. Separate each number with a comma and a space. Use 0 to represent a blank "
              "space")
        initial_state = [input("Enter the first row: "), input("Enter the second row: "),
                         input("Enter the third row: ")]

        for i in range(0, 3):
            # split each row into an array of 3 elements
            initial_state[i] = initial_state[i].split(", ")
            # convert each string array to int array
            initial_state[i] = [int(x) for x in initial_state[i]]

        check_input = True
        # check if input is valid
        # doesn't check if it can be solved, only checks if there is 1 of each number from 0-8
        for i in range(0, 9):
            # check count of each number is 1
            count = initial_state[0].count(i) + initial_state[1].count(i) + initial_state[2].count(i)
            if count != 1:
                check_input = False

        if check_input:
            break
        else:
            print("Invalid Input. Initial state must contain one of each number from 1-8 with 0 as a blank")

    heuristics = Heuristics(initial_state)

    # call corresponding algorithm
    choice = 0
    print("1. Uniform Cost Search")
    print("2. A* Search with Misplaced Tile Heuristic")
    print("3. A* Search with Manhattan Distance Heuristic\n")
    while True:
        choice = input("Choose which algorithm to use by entering the number next to it: ")
        if choice not in ["1", "2", "3"]:
            print("Invalid input. Please enter a number from 1-3 for the corresponding search.\n")
        else:
            break

    if choice == "1":
        heuristics.uniform_cost_search()
    elif choice == "2":
        heuristics.a_star_misplaced_tile()
    elif choice == "3":
        heuristics.a_star_manhattan_distance()

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # call main
    main()
