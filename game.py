import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board # list of bools, where True if that entry of self.board is ' ' and otw False
    
    def num_empty_squares(self):
        # return self.board.count(' ')
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # check first if square is on a diagonal at all, which are the spots 0,2,4,6,8, i.e. it's even
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2,4,6]] # right to left diagonal
            if all([spot == letter for spot in diagonal_2]):
                return True
            
        return False # if all checks fail


def play_game(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}.')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter
        
            letter  = 'O' if letter == 'X' else 'X'
        
        if print_game:
            time.sleep(1)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = GeniusComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        winner = play_game(t, x_player, o_player, print_game=False)
        if winner == 'X':
            x_wins += 1
        elif winner == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'Player X won {x_wins} times, player O won {o_wins} times, and there were {ties} ties.')