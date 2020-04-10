import random 

class Player:
    def __init__(self, player_name, player_token): #Creates class that defines the input for user name and choice of token.
        self.player_name = player_name
        self.player_token = player_token
    
    
#[['x', 'o', 'o'], ['o', 'x', 'o'], ['o', 'x', 'o']] --> some visual representation with a normal tic-tac-to layout
class Game:
    def __init__(self, board, player1, player2):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]   
        self.player1 = player1
        self.player2 = player2

    def __repr__(self, visual_board): #Returns a pretty string representation of the game board
        self.visual_board = [ 
                        [" ","|"," ",'|'," "],  #Printable board
                        ["-","-","-","-","-"],
                        [" ","|"," ","|"," "],
                        ["-","-","-","-","-"],
                        [" ","|"," ","|"," "]
                       ]
             
    def move(self): #Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        possible_moves = {
                          1 : board[0][0],
                          2 : board[0][1],
                          3 : board[0][2],
                          4 : board[1][0],
                          5 : board[1][1], 
                          6 : board[1][2],
                          7 : board[2][0],
                          8 : board[2][1],
                          9 : board[2][2]
                         }
        
        coordinates = {
                       board[0][0] : play_board[0][0],  # coordinates that translate the entries into the board (logical representation)
                       board[0][1] : play_board[0][2],  # into the visual board to be printed
                       board[0][2] : play_board[0][4], 
                       board[1][0] : play_board[2][0], 
                       board[1][1] : play_board[2][2], 
                       board[1][2] : play_board[2][4],
                       board[2][0] : play_board[4][0],
                       board[2][1] : play_board[4][2]
                      }

            player_move = possible_moves[player_input]
            board_position = coordinates[player_input]
        
            if self.board(player_move) == '':
                self.board.append(player_move) #can you append to board if it's inside a different function? -LN
                self.visual_board.append(board_position)
            else:
                print('That position is has been played.')

    def calc_winner(self): #What token character string has won or None if no one has.
        winning_combos = [
                          ['1','2','3']
                          ['4','5','6']
                          ['7','8','9']
                          ['1','4','7']
                          ['2','5','8']
                          ['3','6','9']
                          ['1','5','9']
                          ['3','5','7']
                         ]
        
#             if:
#                 pass
#             #then winning result
        
#             else:
#                 pass
#                 #continue playing
       
    
#     def is_full(self): #Returns true if the game board is full.
#           count = 0
#           if count == 9:
#             count += 1
#             print("It's a tie!")
    
#     def is_game_over(self): #Returns true if the game board is full or a player has won.
#         if count == 9:
#             print("Game over")
#             print("It's a tie!")

def main():

    while True:
        play = input('Would you like to play a game of Tic-tac-toe?\n Type: yes OR no')
        if play == 'yes':
            continue
        elif play == 'no':
            break
        
        input_name1 = input('Player 1 please enter your name: ')
        input_token1 = input('Would you like X\'s or O\'s? : ').lower()
        if token == 'o':
            return 'O'
        else:
            token == 'x'
            return 'X'
        
        
        input_name2 = input('Player 2 please enter your name: ')
        input_token2 = input('Would you like X\'s or O\'s? : ').lower()
        if token == 'o':
            return 'O'
        else:
            token == 'x'
            return 'X'

        player1 = Player(input_name1, input_token)
        player1_moves = []
        
        player2 = Player(input_name2, input_token2)
        player2_moves = []

        game = Game(player1, player2)

        while True:
            print('1|2|3')
            print('4|5|6')
            print('7|8|9')
            player_input = input('Please enter the position to place your piece (1-9): ')
            
            


# def col_win(board,player):
#     for x in range (len(board)):
#         win = True

#         for y in range(len(board)):
#             if board [y][x] != player:
#                 win = False 
#                 continue
        
#         if win == True: 
#             return(win)
    
#     return(win)
    
# print("The winner is:"+ str(play_game()))

main()
