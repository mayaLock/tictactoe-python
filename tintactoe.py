"""
    tictactoe.py
    by Dipayan Sarker
    April 14, 2020
"""

import enum
import os
import random
import sys


def clear():
    os.system('cls')


class PlayerData(enum.Flag):
    NONE = 0
    X = 1
    O = 2


class PlayerType(enum.Flag):
    HUMAN = 0
    COM = 1


class TicTacToe(object):

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board_logical = [PlayerData.NONE for _ in range(9)]
        self.board_graphical = []
        self.current_player = PlayerType.HUMAN
        self.game_count = 1
        self.computer_score = 0
        self.human_score = 0
        self.draw_score = 0
        self.was_draw = False

    def run(self):
        self.print_board()
        choice = TicTacToe.get_option('Please choose 1 or 2 (1 = You start 2 = Computer starts) ')
        if choice == 1:
            self.current_player = PlayerType.HUMAN
        else:
            self.current_player = PlayerType.COM

        while not self.is_winner() or not self.is_draw():
            if self.current_player == PlayerType.HUMAN:
                self.print_board()
                self.player_move()
                if self.is_winner() or self.is_draw():
                    break
                else:
                    self.current_player = PlayerType.COM
                    continue
            if self.current_player == PlayerType.COM:
                self.print_board()
                self.computer_move()
                if self.is_winner() or self.is_draw():
                    break
                else:
                    self.current_player = PlayerType.HUMAN
                    continue
        if not self.was_draw:
            print('%s' % 'You win\n' if self.current_player == PlayerType.HUMAN else 'Computer Wins')
        else:
            print('It\'s a draw!\n\n')
        choice = TicTacToe.get_option('Please choose 1 or 2 (1 = play again 2 = quit) ')
        if choice == 1:
            self.reset()
            self.run()
        else:
            sys.exit(0)
                
    def is_winner(self):
        if self.board_logical[0] != PlayerData.NONE and \
                (self.board_logical[0] & self.board_logical[1] & self.board_logical[2]) == self.board_logical[0] \
        or self.board_logical[3] != PlayerData.NONE and \
                (self.board_logical[3] & self.board_logical[4] & self.board_logical[5]) == self.board_logical[3] \
        or self.board_logical[6] != PlayerData.NONE and \
                (self.board_logical[6] & self.board_logical[7] & self.board_logical[8]) == self.board_logical[6] \
        or self.board_logical[0] != PlayerData.NONE and \
                (self.board_logical[0] & self.board_logical[3] & self.board_logical[6]) == self.board_logical[0] \
        or self.board_logical[1] != PlayerData.NONE and \
                (self.board_logical[1] & self.board_logical[4] & self.board_logical[7]) == self.board_logical[1] \
        or self.board_logical[2] != PlayerData.NONE and \
                (self.board_logical[2] & self.board_logical[5] & self.board_logical[8]) == self.board_logical[2] \
        or self.board_logical[0] != PlayerData.NONE and \
                (self.board_logical[0] & self.board_logical[4] & self.board_logical[8]) == self.board_logical[0] \
        or self.board_logical[2] != PlayerData.NONE and \
                (self.board_logical[2] & self.board_logical[4] & self.board_logical[6]) == self.board_logical[2]:
            return True
        return False
        
    @staticmethod
    def get_option(prompt):
        while True:
            try:
                x = int(input(prompt))
            except ValueError:
                continue
            else:
                if x in range(1, 3):
                    return x

    def reset(self):
        clear()
        self.board_logical.clear()
        self.board_logical = [PlayerData.NONE for _ in range(9)]
        self.board_graphical.clear()
        self.game_count += 1
        self.was_draw = False

    def print_board(self):
        self.convert_logical_to_graphical_board()
        clear()
        if not self.was_draw and self.is_winner():
            if self.current_player == PlayerType.HUMAN:
                self.human_score += 1
            else:
                self.computer_score += 1
        if self.was_draw:
            self.draw_score += 1

        print('TicTacToe by Dipayan Sarker\n\n  %s  |  %s  |  %s  \n-----------------\n  %s  |  %s  |  %s'
              '  \n-----------------\n  %s  |  %s  |  %s  \n\nGame number\t\t %d\nYour Score\t\t %d\nComputer\'s '
              'score\t %d\nDraw score\t\t %d\n\n' %
              (self.board_graphical[0],
               self.board_graphical[1],
               self.board_graphical[2],
               self.board_graphical[3],
               self.board_graphical[4],
               self.board_graphical[5],
               self.board_graphical[6],
               self.board_graphical[7],
               self.board_graphical[8],
               self.game_count,
               self.human_score,
               self.computer_score,
               self.draw_score))
        
    def convert_logical_to_graphical_board(self):
        self.board_graphical = [' ' if i == PlayerData.NONE else 'X' if i == PlayerData.X else 'O'
                                for i in self.board_logical]

    def set_game_pos(self, i, player):
        if self.is_free_spot(i):
            self.board_logical[i-1] = player
            return True
        return False

    def is_draw(self):
        if PlayerData.NONE not in self.board_logical:
            self.was_draw = True
            self.print_board()
            return True
        return False

    def is_free_spot(self, i):
        return self.board_logical[i-1] == PlayerData.NONE

    def computer_move(self):
        com_pos_rand = 10
        while not self.is_draw() or not self.is_free_spot(com_pos_rand):
            com_pos_rand = random.randint(1, 9)
            if self.is_free_spot(com_pos_rand):
                self.set_game_pos(com_pos_rand, PlayerData.O)
                break
        self.print_board()

    @staticmethod
    def get_player_input():
        while True:
            try:
                x = int(input('Please choose a position (1-9) '))
            except ValueError:
                continue
            else:
                if x in range(1, 10):
                    return x

    def player_move(self):
        player_input = 10
        while not self.is_draw() or not self.is_free_spot(player_input):
            player_input = TicTacToe.get_player_input()
            if self.is_free_spot(player_input):
                self.set_game_pos(player_input, PlayerData.X)
                break
        self.print_board()

    
if __name__ == '__main__':
    game_obj = TicTacToe()
    game_obj.run()
