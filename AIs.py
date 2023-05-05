from random import randint,choice as rand
from time import sleep
WINS=[(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

            
class DummAI(object):
    def __init__(self,game_dict):
        self.gamedict = game_dict
        self.move = self.think()
    def think (self):
        pos = randint(1,9)
        while not self.gamedict[pos] == ' ':
            pos = randint(1,9)
        return pos

class HorseAI(DummAI):

    def think(self):
        #first moves
        good_moves = [1,3,5,7,9]
        while self.gamedict[5]==' ':
            try:
                init_move = rand(good_moves)
                assert self.gamedict[init_move] == ' '
                return init_move
            except AssertionError:
                continue
        
        #will be used to chose the best move
        good_moves = []
        block_moves = []
        #check for blockings or return a winning move
        for (a,b,c) in WINS:
                if self.gamedict[a]=='X' and self.gamedict[b]=='X' and self.gamedict[c] == ' ':
                    block_moves.append(c)
                elif self.gamedict[a]=='O' and self.gamedict[b]=='O' and self.gamedict[c] == ' ':
                    return c
                elif self.gamedict[a]=='X' and self.gamedict[c]=='X' and self.gamedict[b] == ' ':
                    block_moves.append(b)
                elif self.gamedict[a]=='O' and self.gamedict[c]=='O' and self.gamedict[b] == ' ':
                    return b  
                elif self.gamedict[b]=='X' and self.gamedict[c]=='X' and self.gamedict[a] == ' ':
                    block_moves.append(a)
                elif self.gamedict[b]=='O' and self.gamedict[c]=='O' and self.gamedict[a] == ' ':
                    return a                    
                #catch good spots for playing
                elif 'X' not in [self.gamedict[a],self.gamedict[b],self.gamedict[c]]:
                    good_moves += [move for move in [a, b, c] if self.gamedict[move] == ' ']

        # makes a block
        if block_moves != []:
            return rand(block_moves)
        # filters good moves
        if good_moves != [] and good_moves != list(set(good_moves)):
            for (a,b,c) in WINS:
                if a in good_moves and (self.gamedict[b] == 'X' or self.gamedict[c] == 'X') :
                    good_moves.remove(a)
                if b in good_moves and (self.gamedict[a] == 'X' or self.gamedict[c] == 'X') :
                    good_moves.remove(b)
                if  c in good_moves and (self.gamedict[b] == 'X' or self.gamedict[a] == 'X'):
                    good_moves.remove(c)   
        # make a good move
        if good_moves != []: 
            return rand(good_moves)    
        # makes a meh move (will probably result in draw)
        meh_moves = [key for key,value in self.gamedict.items() if value == ' ']
        return rand(meh_moves)
        #make a good move



