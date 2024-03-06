from random import choice, shuffle


SYMBOLS = [' X ', " O "]


class Board:
    def __init__(self) -> None:
        self.boardstate = [["   " for _ in range(3)] for _ in range(3)]

    def __str__(self) -> str:
        string_rep = "\n"
        for line in self.boardstate:
            string_rep+="|".join(line)
            string_rep+="\n-----------\n"
        return string_rep[:-len("-----------\n")]
    
    def is_ended(self):
        for i in range(len(self.boardstate)):
            if self.boardstate[i][0] == self.boardstate[i][1] == self.boardstate[i][2] != "   ":
                return self.boardstate[i][0]
            elif self.boardstate[0][i] == self.boardstate[1][i] == self.boardstate[2][i] != "   ":
                return self.boardstate[0][i]
        if self.boardstate[0][0] == self.boardstate[1][1] == self.boardstate[2][2] != "   ":
            return self.boardstate[0][0]
        if self.boardstate[2][0] == self.boardstate[1][1] == self.boardstate[0][2] != "   ":
            return self.boardstate[2][0]
        return None
    
    def make_move(self, tag,  row, column):
        self.boardstate[row][column]=tag

    def is_available_move(self, row, column):
        
        if self.boardstate[row][column] == "   " and 0<=row<3 and 0<=column<3:
            return True
        else:
            return False

    def is_full(self):
        for line in self.boardstate:
            if "   " in line:
                return False
        return True



class Player:
    def __init__(self,tag:str, isai:bool=False) -> None:
        self.isai=isai
        self.symbol = tag


    def move(self, board_state: Board):
        if self.isai:
            pass
        else:
            single_move = [-1,-1]
            while not board_state.is_available_move(single_move[0]-1,single_move[1]-1):
                suggested_move = input(f'Please provide a move for{self.symbol}player as x,y to say the row and column: ')
                try:
                    single_move = [int(x) for x in suggested_move.split(',')]
                    if not board_state.is_available_move(single_move[0]-1,single_move[1]-1):
                        print('This square is already taken!')
                except:
                    print('You have provided an incorrect input, try again.')
                    single_move = [-1,-1]
            board_state.make_move(self.symbol, single_move[0]-1, single_move[1]-1)
                
class AI_player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def move(self, board:Board):
        imporant_move = []
        possible_move = []
        opponent_symbol = SYMBOLS[0] if self.symbol == SYMBOLS[1] else SYMBOLS[1]
        for row in range(len(board.boardstate)):
            for col in range(len(board.boardstate[row])):
                if board.boardstate[row][col] == '   ':
                    board.boardstate[row][col]=self.symbol
                    if board.is_ended(): 
                        board.boardstate[row][col]="   "
                        board.make_move(self.symbol, row, col)
                        print(row, col) 
                        return
                    else:
                        board.boardstate[row][col]=opponent_symbol
                        if board.is_ended():
                            imporant_move = [row,col]
                        board.boardstate[row][col]="   "
                    possible_move.append([row,col])
        if imporant_move == []:
            move = choice(possible_move)
            board.make_move(self.symbol, move[0], move[1])    
        else:
            board.make_move(self.symbol, imporant_move[0], imporant_move[1])
        return


class Game_ui:
    def __init__(self) -> None:
        self.players = SYMBOLS
        self.turn = 0
    
    def greetings(self):
        print(f'Hello, you can play a Tic-Tac-Toe with your friends or AI')
        
    
    def choose_ai(self):
        answer = ''
        while not (answer == 'y' or answer =='n'):
            answer = input("Do you wanna play vs AI ? Type 'y' to continue and 'n' to play 2 Players game: ").lower()
        if answer=='y': 
            return True
        else: 
            return False

    def randomize_players(self, player_1, player_2):
        gamers = [player_1,player_2]
        shuffle(gamers)
        player_1, player_2 = gamers[0], gamers[1]
        player_1.symbol, player_2.symbol = SYMBOLS[0], SYMBOLS[1]
        return [player_1,player_2]

    def main_loop(self, player_1:Player, player_2:Player):
        is_repeat = True
        if self.choose_ai():
            player_2=AI_player(player_2.symbol)
        # chose vs AI
        while is_repeat:
            players = self.randomize_players(player_1, player_2)
            player_1 = players[0]
            player_2=players[1]
            current_player=player_2
            board= Board()
            self.greetings()
            while not (board.is_ended() or board.is_full()):
                current_player=player_2 if current_player==player_1 else player_1
                if isinstance(current_player, Player):
                    print(board)
                current_player.move(board)
            print(board)
            if board.is_ended():
                print(f'Congratulation to player {current_player.symbol[1]}!')
            else:
                print("It's a draw!")

            is_repeat = self.ask_if_continue()
        print('Thank you for playing!')

    def ask_if_continue(self)-> bool:
        answer = ''
        while not (answer == 'y' or answer =='n'):
            answer = input("Do you wanna play again? Type 'y' to continue and 'n' to exit: ").lower()
        if answer=='y': 
            return True
        else: 
            return False





game = Game_ui()
game.main_loop(Player(SYMBOLS[0]), Player(SYMBOLS[1]))