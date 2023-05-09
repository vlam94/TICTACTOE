from random import randint ,choice as rand
from time import sleep 
from AIs import DummAI, HorseAI

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
        ai=HorseAI(self.gamedict,'O')
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

# 'X' = DummAI
class Rand_TicTacToe(TicTacToe):
    def __init__(self):
        super().__init__()
        self.log = []
        self.result = "tie"   
        

    def x_move(self):
        move = self.get_x_move()
        if 'X' in self.gamedict.values() and 'O' in self.gamedict.values():
            self.register_log(move,'X')
        self.make_move('X',move) 
        self.play('O')

    def get_x_move(self):
        ai2 = DummAI(self.gamedict)
        return ai2.move
    
    def get_ai_move(self):
        ai = HorseAI(self.gamedict,'O')
        return ai.move
    
    def ai_move(self):
        move = self.get_ai_move()
        if 'X' in self.gamedict.values() and 'O' in self.gamedict.values():
            self.register_log(move,'O')
        self.make_move('O',move)
        self.play('X')

    # def start(self):
    #     cointoss = randint(0,1)
    #     if cointoss:
    #         self.play('X')
    #     self.play('O')
    def register_log(self,move,turn):
        tuple_state = []
        for mark in self.gamedict.values():
            if mark == turn:
                space = (1,0)
            elif mark != ' ':
                space = (0,1)
            else:
                space = (0,0)
            tuple_state.append(space)
        move_reg = [0,0,0,0,0,0,0,0,0]
        move_reg[move-1]=1
        self.log.append((tuple(tuple_state),tuple(move_reg)))
        
        
    def play(self,whoseturn):
        #print(self)
        if ' ' not in self.gamedict.values():
            raise TIE()
        
        if self.detect_win():
            if whoseturn == 'X':
                self.result = 'lose'
            else:
                self.result = 'win'
            raise GAMEOVER
        
        if whoseturn == 'X':
            self.x_move()
        else:
            self.ai_move()
            
while __name__=='__main__':
   try:
       game = TicTacToe()
       game.start()
   except GAMEOVER:
      print('GAME OVER !')
   if input("Type 'E' to Exit or ↵ to play again: ").upper().startswith('E'):
       exit()