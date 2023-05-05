from game import GAMEOVER,TIE, Rand_TicTacToe
import os

ds_path = 'ttt_ds.csv'
if os.path.getsize(ds_path) > 13:
    if input("\nWHOA! It seems you've already created the data_set!\nContinuing will double it's size!\n\nDo you wish to continue <y/n>: ").upper().startswith('N'):
        exit()

x=0
o=0
t=0
max_streak=0
streak = 0
with open(ds_path,mode='a') as f:
    for _ in range(420000):
        try:
            game = Rand_TicTacToe()
            game.play('X')
        except GAMEOVER:
            if game.result == 'win':
                streak = 0
                x += 1
                #print('\n\n\n X WINS ! \n\n\n')
                #print(game)
                #sleep(15)
            else:
                streak += 1
                o += 1
            if streak > max_streak:
                max_streak = streak            
        except TIE:
            t += 1
        
        plays = []
        for i in range (9):
            try:
                plays.append(game.log[i])
            except IndexError:
                plays.append("?")
        plays.append(game.result)
        #print(game)
        #print(plays)
        #sleep(2)
        plays = str(plays).strip("][")
        f.write(plays.replace("'", ""))
        f.write('\n')
    
print (f"The DummAI has won {x} times\nThe HorseAI has won {o} times\nand there has been {t} ties\nMax Horse Streak was {max_streak} wins in a row\n")
