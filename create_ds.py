from game import GAMEOVER,TIE, Rand_TicTacToe
import os
import pickle as pickle_rick

ds_path = 'ttt_ds.pkl'
if os.path.getsize(ds_path) > 13:
    print ("\nWHOA! It seems you've already created the data_set!\nContinuing will overwrite it\n\n ABORTING!\n")
    exit()
x=0
o=0
t=0
max_streak=0
streak = 0
#with open(ds_path, mode = 'w') as f:
     #f.write('[')
num_wins = 33000
logs=[]
while x < num_wins:
    if x % 1000 == 0:
        print('still processing...')  
    try:
        game = Rand_TicTacToe()
        game.play('X')
    except GAMEOVER:
        if game.result == 'win':
            for i in range(len(game.log)):
                if i % 2 == 0:
                    #saves moves to the winning random player
                    #print(f"X WIN {game.log[i]}")
                    logs.append(game.log[i]) 
            streak = 0
            x += 1
            #print('\n\n\n X WINS ! \n\n\n')
            #print(game)
            #sleep(15)
        else: 
            streak += 1
            o += 1
        if o % 15 == 0 and game.result=='lose':
            for i in range(len(game.log)):
                if i % 2 == 1:
                    #saves moves to the winning strategic player
                    #print(f"O WIN {game.log[i]}")
                    logs.append(game.log[i])
           
            
        if streak > max_streak:
            max_streak = streak
        #with open(ds_path, 'a') as f:
            #json.dump(logs, f)
            #f.write(',\n')
        
    except TIE:
        t += 1
        if t % 5 == 0:
            for i in range(len(game.log)):
                if i % 2 == 1:
                    #saves strategic moves of the TIE
                    #print(f"TIE {game.log[i]}")
                    logs.append(game.log[i])
    

    #for play in logs:
    #   print(play)
#with open(ds_path, mode='r+b') as f:
    #f.seek(-2, os.SEEK_END)
    #f.write(b']')


print (f"The DummAI has won {x} times\nThe HorseAI has won {o} times\nand there has been {t} ties\nMax Horse Streak was {max_streak} wins in a row\n\n{x+o+t} matches were played\n")
with open(ds_path, "wb") as f:
    pickle_rick.dump(logs, f)

    