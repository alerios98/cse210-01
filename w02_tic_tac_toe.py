def main():
    print('hi')
    grid_list = create_grid()
    grid = display_grid(grid_list)
    score = ''

    while score != 'win':
        player_turn_x = turn_x(grid_list)
        grid = display_grid(player_turn_x)

        player_turn_y = turn_y(grid_list)
        grid = display_grid(player_turn_y)

        if grid_list[0] == grid_list[1] == grid_list[0]:
            score = 'win'
        elif grid_list[3] == grid_list[4] == grid_list[5]:
            score = 'win'
        elif grid_list[6] == grid_list[7] == grid_list[8]:
            score = 'win'
        elif grid_list[0] == grid_list[3] == grid_list[6]:
            score = 'win'
        elif grid_list[1] == grid_list[4] == grid_list[7]:
            score = 'win'
        elif grid_list[2] == grid_list[5] == grid_list[8]:
            score = 'win'
    
    print('The game is over')

#creates a list with the number of positions on grid
def create_grid():
    grid = []
    for i in range(1,10):
        grid.append(i)
    return grid

# #using the list it can display the grid using print statements and indeces
def display_grid(grid):
    print(f'{grid[0]}|{grid[1]}|{grid[2]}')
    print('-+-+-')
    print(f'{grid[3]}|{grid[4]}|{grid[5]}')
    print('-+-+-')
    print(f'{grid[6]}|{grid[7]}|{grid[8]}')

def turn_x(grid_list):
    position = int(input("x's turn to choose a square (1-9) "))
    grid_list[position - 1] = 'x'
    return grid_list
        

def turn_y(grid_list):
    position = int(input("o's turn to choose a square (1-9) "))
    grid_list[position - 1] = 'o'
    return grid_list

if __name__ == '__main__':
    main()