def main():
    print('hi')
    grid_list = create_grid()
    grid = display_grid(grid_list)
    score = ''
    
    while score != True:
        player1 = turn_x(grid_list)
        print(grid_list)

        player2 = turn_o(grid_list)
        print(grid_list)

        score = winner(grid_list,score)

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
    board = display_grid(grid_list)
    return board
        

def turn_o(grid_list):
    position = int(input("o's turn to choose a square (1-9) "))
    grid_list[position - 1] = 'o'
    board = display_grid(grid_list)
    return board

def winner(grid_list,score):
    if grid_list[0] == grid_list[1] == grid_list[0]:
        return score == True
    elif grid_list[3] == grid_list[4] == grid_list[5]:
        return score == True
    elif grid_list[6] == grid_list[7] == grid_list[8]:
        return score == True
    elif grid_list[0] == grid_list[3] == grid_list[6]:
        return score == True
    elif grid_list[1] == grid_list[4] == grid_list[7]:
        return score == True
    elif grid_list[2] == grid_list[5] == grid_list[8]:
        return score == True
    else:
        return score == False

if __name__ == '__main__':
    main()