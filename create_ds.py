from game import GAMEOVER,TIE, Rand_TicTacToe
import json
import os
import pickle

ds_path = 'ttt_ds.pkl'
if os.path.getsize(ds_path) > 13:
    print ("\nWHOA! It seems you've already created the data_set!\nContinuing will fuck it UP\n\n ABORTING!\n")
    #exit()

x=0
o=0
t=0
max_streak=0
streak = 0
#with open(ds_path, mode = 'w') as f:
     #f.write('[')
num_wins = 20
logs=[]
while x < num_wins:
      
    try:
        game = Rand_TicTacToe()
        game.play('X')
    except GAMEOVER:
        if game.result == 'win':
            for play in game.log:
                play[1][1] = 1
                logs.append(play) 
            streak = 0
            x += 1
            #print('\n\n\n X WINS ! \n\n\n')
            #print(game)
            #sleep(15)
        else:
            streak += 1
            o += 1
            for play in game.log:
                logs.append(play)
        if streak > max_streak:
            max_streak = streak
        #with open(ds_path, 'a') as f:
            #json.dump(logs, f)
            #f.write(',\n')
        
    except TIE:
        t += 1
    

    #for play in logs:
    #   print(play)
#with open(ds_path, mode='r+b') as f:
    #f.seek(-2, os.SEEK_END)
    #f.write(b']')


print (f"The DummAI has won {x} times\nThe HorseAI has won {o} times\nand there has been {t} ties\nMax Horse Streak was {max_streak} wins in a row\n\n{x+o+t} matches were played\n")
with open(ds_path, "wb") as f:
    pickle.dump(logs, f)

    