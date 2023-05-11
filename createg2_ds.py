from game import GAMEOVER,TIE, Clash_Of_AIs
from os.path import getsize
import pickle as pickle_rick


##this script won't overwrite datasets!
#try: 
ds_path = 'tttg22_ds.pkl'
#    assert getsize(ds_path) < 13, "\nWHOA! It seems you've already created the data_set!\nContinuing will overwrite it\n\n ABORTING!\n"
#except AssertionError as e:
#    print (e)
#    exit()
    

x=0
o=0
t=0

#num_wins = 270420
logs=[]
print('starting process...\n')
for _ in range(1000000):  
    try:
        game = Clash_Of_AIs()
        game.play('X')
    except GAMEOVER:
        if game.result == 'win':
            for i in range(len(game.log)):
                if not (i % 2):
                    #saves moves from the winning strategic player side
                    #print(f"X WIN {game.log[i]}")
                    logs.append(game.log[i]) 
            x += 1
            #print('\nstill processing...')
        else: 
            #Disconsiders NNAI victories
            o += 1
                    
    except TIE:
        t += 1
        for i in range(len(game.log)):
            #saves ALL moves from the TIE
            #print(f"TIE {game.log[i]}")
            logs.append(game.log[i])
    if not (_ % 5000):     
        print(f"process at {_/10000} %\n")



print (f"The HorseAI has won {x} times\nThe NNAI has won {o} times\nand there has been {t} ties were registred\n")
print(f"a total of {x+t} matches were registred")
with open(ds_path, "wb") as f:
    pickle_rick.dump(logs, f)