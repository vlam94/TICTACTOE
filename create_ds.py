from game import GAMEOVER,TIE, Rand_TicTacToe
from os.path import getsize
import pickle as pickle_rick


#this script won't overwrite datasets!
try: 
    ds_path = 'tttg2_ds.pkl'
    assert getsize(ds_path) < 13, "\nWHOA! It seems you've already created the data_set!\nContinuing will overwrite it\n\n ABORTING!\n"
except AssertionError as e:
    print (e)
    exit()
    

x=0
o=0
t=0
ocut = 23
tcut = 2
num_wins = 100000
logs=[]
print('starting process...\n')
while x < num_wins:  
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
            x += 1
            if x and x % 10000 == 0:
                print('\nstill processing...')
        else: 
            o += 1
        # saving every {n in o % n} X victory match  
        if o % ocut == 0 and game.result=='lose':
            for i in range(len(game.log)):
                if i % 2 == 1:
                    #saves moves to the winning strategic player
                    #print(f"O WIN {game.log[i]}")
                    logs.append(game.log[i])
                    
    except TIE:
        t += 1
        if t % tcut == 0:
            for i in range(len(game.log)):
                if i % 2 == 1:
                    #saves strategic moves of the TIE
                    #print(f"TIE {game.log[i]}")
                    logs.append(game.log[i])
    



print (f"The DummAI has won {x} times\nThe HorseAI has won {o} times\nand there has been {t} ties\n\n{int(o/ocut)} O wins were registred, {int(t/tcut)} ties were registred\n")
print(f"a total of {x+int(o/ocut)+int(t/tcut)} matches were registred")
with open(ds_path, "wb") as f:
    pickle_rick.dump(logs, f)

    