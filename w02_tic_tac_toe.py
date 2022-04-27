board = {'1': '1','2': '2','3': '3',
'4': '4','5': '5','6': '6',
'7': '7','8': '8','9': '9'}

def main():
    turn = 'x'
    count = 0
    
    for i in range(10):
        display_board(board)
        print()
        move = input(f"it is {turn}'s turn. Where do you want to move? ")
        print()

        if board[move] != 'x' or board[move] != 'o':
            board[move] = turn
            count += 1
                
        if count >= 5:
            if board['7'] == board['8'] == board['9'] : # across the bottom
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')                
                break
            elif board['4'] == board['5'] == board['6'] : # across the middle
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break
            elif board['1'] == board['2'] == board['3']: # across the top
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break
            elif board['1'] == board['4'] == board['7'] : # down the left side
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break
            elif board['2'] == board['5'] == board['8'] : # down the middle
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break
            elif board['3'] == board['6'] == board['9'] : # down the right side
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break 
            elif board['7'] == board['5'] == board['3'] : # diagonal
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break
            elif board['1'] == board['5'] == board['9'] : # diagonal
                display_board(board)
                print()
                print('Game Over')                
                print(f'{turn} won the game!')  
                break 
        
        if count == 9:
            print("Game over! It's a tie")
        
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    

def display_board(board):
    print(board['1']+ '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4']+ '|' + board['5'] + '|' + board['6']) 
    print('-+-+-')
    print(board['7']+ '|' + board['8'] + '|' + board['9'])

if __name__ == '__main__':
    
    play_again = ''
    while play_again != 'no':
        main()
        play_again = input('would you like to play again (yes/no)? ').lower()
        if play_again == 'yes':
            board = {'1': '1','2': '2','3': '3',
            '4': '4','5': '5','6': '6',
            '7': '7','8': '8','9': '9'}