from random import randint,choice as rand
from time import sleep
from keras.models import load_model
import numpy as np
WINS=[(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

            
class DummAI(object):
    def __init__(self,game_dict):
        self.gamedict = game_dict
        self.move = self.think()

    def think(self):
        pos = randint(1,9)
        while not self.gamedict[pos] == ' ':
            pos = randint(1,9)
        return pos

class HorseAI(object):

    def __init__(self,game_dict,mark):
        self.gamedict = game_dict
        self.isx = bool(mark=='X')
        self.move = self.think()
        
        

    def think(self):
        # #first moves
        # good_moves = [1,3,5,7,9]
        # while self.gamedict[5]==' ':
        #     try:
        #         init_move = rand(good_moves)
        #         assert self.gamedict[init_move] == ' '
        #         return init_move
        #     except AssertionError:
        #         continue
        if self.isx:
            x='O' #inverted bc they are looking for adversary plays
            o='X' #and it was originally playing as 'O'
        else:
            x='X'
            o='O'
        #will be used to chose the best move
        good_moves = []
        block_moves = []
        #check for blockings or return a winning move
        for (a,b,c) in WINS:
                if self.gamedict[a]==x and self.gamedict[b]==x and self.gamedict[c] == ' ':
                    block_moves.append(c)
                elif self.gamedict[a]==o and self.gamedict[b]==o and self.gamedict[c] == ' ':
                    return c
                elif self.gamedict[a]==x and self.gamedict[c]==x and self.gamedict[b] == ' ':
                    block_moves.append(b)
                elif self.gamedict[a]==o and self.gamedict[c]==o and self.gamedict[b] == ' ':
                    return b  
                elif self.gamedict[b]==x and self.gamedict[c]==x and self.gamedict[a] == ' ':
                    block_moves.append(a)
                elif self.gamedict[b]==o and self.gamedict[c]==o and self.gamedict[a] == ' ':
                    return a                    
                #catch good spots for playing
                elif x not in [self.gamedict[a],self.gamedict[b],self.gamedict[c]]:
                    good_moves += [move for move in [a, b, c] if self.gamedict[move] == ' ']

        # makes a block
        if block_moves != []:
            return rand(block_moves)
        # filters good moves
        if good_moves != [] and good_moves != list(set(good_moves)):
            for (a,b,c) in WINS:
                if a in good_moves and (self.gamedict[b] == x or self.gamedict[c] == x) :
                    good_moves.remove(a)
                if b in good_moves and (self.gamedict[a] == x or self.gamedict[c] == x) :
                    good_moves.remove(b)
                if  c in good_moves and (self.gamedict[b] == x or self.gamedict[a] == x):
                    good_moves.remove(c)   
        # make a good move
        if good_moves != []: 
            return rand(good_moves)    
        # makes a meh move (will probably result in draw)
        meh_moves = [key for key,value in self.gamedict.items() if value == ' ']
        return rand(meh_moves)
        #make a good move

class NNAI(DummAI):
    model = load_model('E:\Desktop\Ferramentas\GITs\TICTACTOE\\tic_tac_toe_model.h5')
    def __init__(self, game_dict,mark):
        self.gamedict = game_dict
        self.mark = mark
        self.move = self.think()
    
    
    def board_to_bin(self):
        bin_board = []
        for mark in self.gamedict.values():
            if mark == self.mark:
                space = (1,0)
            elif mark != ' ':
                space = (0,1)
            else:
                space = (0,0)
            bin_board.append(space)
        bin_board = np.array(bin_board).flatten()
        return bin_board.reshape(1, -1)
    
    
    def prob_to_move(self,prob_move):
        while True:
            try:
                move=int(np.argmax(prob_move)+1)
                assert self.gamedict[move] == ' '
                return move
            except AssertionError:
                prob_move = np.delete(prob_move,(move-1))
                print("\nthinkin' hard...")
        
                
    def think(self):
        if 'X' not in self.gamedict.values() and 'O' not in self.gamedict.values():
            return randint(1,9)
        bin_board = self.board_to_bin()
        prob_move = self.model(bin_board)
#        prob_move = self.model(bin_board,verbose=0)
        return self.prob_to_move(prob_move)
        