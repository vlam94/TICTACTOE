from random import randint ,choice as rand
from time import sleep 

WINS=[(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


class GAMEOVER (Exception):
    pass

class TIE (Exception):
    pass

class TicTacToe (object):
    def __init__ (self):
        self.gamedict = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
    
    def __str__(self):
        ret =f"\n {self.gamedict[1]} | {self.gamedict[2]} | {self.gamedict[3]} "
        ret +="\n---+---+---\n"
        ret +=f" {self.gamedict[4]} | {self.gamedict[5]} | {self.gamedict[6]} "
        ret +="\n---+---+---\n"
        ret +=f" {self.gamedict[7]} | {self.gamedict[8]} | {self.gamedict[9]} \n"
        return ret 

    # human will always use X
    def make_move(self,mark,pos):
        self.gamedict[pos]=mark
 
    def get_user_move(self):
        while True:
            try:
                inp= int(input("\nEnter a number between 1 and 9: "))
                assert 1 <= inp <= 9, "\nNumber should be between 1 and 9\n"
                assert self.gamedict[inp] == ' ', "\nPosition already taken, champ!\nTry Again!\n"
                return inp
            except ValueError:
                print("\nInvalid input! Please enter a number.\n")
            except AssertionError as error:
                print(error)

    def human_move(self):
        move = self.get_user_move()
        self.make_move('X',move)
        self.play('O')
        

    def ai_move(self):
        move = self.get_ai_move()
        self.make_move('O',move)
        self.play('X')

    def get_ai_move(self):
        ai=HorseAI(self.gamedict)
        return ai.move
    
    def detect_win(self):
        for (a,b,c) in WINS:
            if self.gamedict[a]==self.gamedict[b]==self.gamedict[c]!=' ':
                return True
        return False

    def start(self):
        print(self)
        inp = input("\ntype 'F' to make the first move\n").upper()
        if inp.startswith('F'):
            self.human_move()    
        self.ai_move()
            
             
    
    def play(self,whoseturn):
        print(self)
        if self.detect_win() or ' ' not in self.gamedict.values():
            raise GAMEOVER
        if whoseturn == 'X':
            self.human_move()
        else:
            self.ai_move()
            
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
        #first play
        if self.gamedict[5]==' ':
            return 5
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



# 'X' = DummAI
class Rand_TicTacToe(TicTacToe):
    def __init__(self):
        super().__init__()
        self.winner= 't'
        self.log = ""   
    
    def x_move(self):
       move = self.get_x_move()
       self.make_move('X',move)
       self.play('O')

    def get_x_move(self):
        ai2 = DummAI(self.gamedict)
        return ai2.move
    
    def get_ai_move(self):
        ai = HorseAI(self.gamedict)
        return ai.move
    def start(self):
        cointoss = randint(0,1)
        if cointoss:
            self.play('X')
        self.play('O')
        
    def play(self,whoseturn):
        #print(self)
        self.log+=str(self)
        if self.detect_win():

            raise GAMEOVER
        self.winner = whoseturn
        if ' ' not in self.gamedict.values():
            raise TIE()
        if whoseturn == 'X':
            self.x_move()
        else:
            self.ai_move()
    
# while __name__=='__main__':
#    try:
#        game = TicTacToe()
#        game.start()
#    except GAMEOVER:
#       print('GAME OVER !')
#    if input("Type 'E' to Exit or ↵ to play again: ").upper().startswith('E'):
#        exit()
x=0
o=0
t=0
max_streak=0
streak = 0
for _ in range(100):
    try:
        game = Rand_TicTacToe()
        game.play('X')
    except GAMEOVER:
        if game.winner == 'X':
            streak = 0
            x += 1
            print('\n\n\n X WINS ! \n\n\n')
            print(game.log)
            #sleep(15)
        else:
            streak += 1
            o += 1
        if streak > max_streak:
            max_streak = streak            
    except TIE:
        #print('\n\n\n GRAVATOU ! \n\n\n')
        t += 1
    #print(game)
    #sleep(2)

    
print (f"The DummAI has won {x} times\nThe HorseAI has won {o} times\nand there has been {t} ties\nMax Horse Streak was {max_streak} wins in a row\n")
