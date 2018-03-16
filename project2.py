"""
ICS 32 Project 2
Author:  UCI_ID: 91605061  Name: Jerry Shen
"""
import connectfour

def print_board(board:[[int]])->None: #called by ask_move()
    """Prints the gameboard"""
    x = 0
    i = 0
    print("1 2 3 4 5 6 7")
    while i < connectfour.BOARD_ROWS:
        while x < connectfour.BOARD_COLUMNS-1:
            print_list = []
            for e in board:
                if e[x] == connectfour.NONE:
                    print_list.append(".")
                elif e[x] == connectfour.RED:
                    print_list.append("R")
                elif e[x] == connectfour.YELLOW:
                    print_list.append("Y")
            x += 1
            print(( '[%s]' % ' '.join(map(str, print_list)))[1:-1])
        i += 1
        
def check_turn_input_int(turn: str)->bool: #called by ask_move()
    """Checks if the turn input is an int"""
    try:
        turn = int(turn)
        if turn >= 1 and turn <= connectfour.BOARD_COLUMNS:
            return True
        else:
            return False
    except ValueError:
        return False

def ask_move(gamestate:["board", "turn"])->str: #called by main()
    """Ask user input for turn"""
    print_board(gamestate.board)
    if gamestate.turn == connectfour.RED:
        while True:
            turn = input("RED's Turn, please enter a number: ")
            if check_turn_input_int(turn)== True:
                turn = int(turn) - 1
                return turn
            else:
                print("Not a valid input, please try again")
    if gamestate.turn == connectfour.YELLOW:
        while True:
            turn = input("YELLOW's Turn, please enter a number: ")
            if check_turn_input_int(turn)== True:
                turn = int(turn) - 1
                return turn
            else:
                print("Not a valid input, please try again")

def check_if_winner(gamestate:["board", "turn"])->None: #called by main()
    """Check if there's a winner"""
    if connectfour.winner(gamestate) == connectfour.RED:
        print("RED wins") 
        return True #ends program if winner
    elif connectfour.winner(gamestate) == connectfour.YELLOW:
        print("YELLOW wins")
        return True #ends program if winner
    else:
        return False #continue program if no winner
    
def check_if_pop(gamestate, player_move)->"gamestate": #called by main()
    """check if pop rules apply to turn"""
    return connectfour.pop(gamestate, player_move) #calls connectfour.py

def check_if_drop(gamestate, player_move)->"gamestate": #called by main()
    """check if drop rules apply to turn"""
    return connectfour.drop(gamestate, player_move) #calls connectfour.py

def main():
    """Creates new game and starts everything"""
    gamestate = connectfour.new_game()
    while True:
        if  check_if_winner(gamestate) == False:
            player_move = ask_move(gamestate)
            try:
                gamestate = check_if_drop(gamestate, player_move)
            except:
                try:
                    gamestate = check_if_pop(gamestate, player_move)
                except:
                    print("Invalid move, try again")
                    player_move = ask_move(gamestate)
        else:
            return
    
if __name__ == '__main__':
    main()
