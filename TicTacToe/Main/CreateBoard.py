

def user_input():
    grid = [0, 0]
    grid[0] = input("Enter X value: ")
    grid[1] = input("Enter Y Value: ")
    return grid


def full_board_builder(grid_x, grid_y):
    full_board_string = "    "
    top_boarder = ""
    for value_x in range(grid_x):
        full_board_string = full_board_string + " {}"
        full_board_string = full_board_string.format(value_x + 1)
        top_boarder = top_boarder + "_ "
    full_board_string = full_board_string + "\n     " + top_boarder + "\n"
    for value_y in range(grid_y):
        full_board_string = full_board_string + row_creation(grid_x, (value_y + 1)) + "\n"

    return full_board_string


def row_creation(grid_x, value_y):
    row_string = "{}   |"
    for value_x in range(grid_x):
        row_string = row_string + "_|"
    return row_string.format(value_y)


def main():
    grid = user_input()
    board = full_board_builder(int(grid[0]), int(grid[1]))
    print(board)


main()