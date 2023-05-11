from game import GAMEOVER,TIE, Clash_Of_AIs
from time import sleep
x=0
o=0
t=0
max_streak=0
streak = 0
logs=[]
for _ in range(1000):
    try:
        game = Clash_Of_AIs()
        game.play('X')
    except GAMEOVER:
        if game.result == 'win':
            x += 1
            streak += 1
            #print('\n\n\n X WINS ! \n\n\n')
            print(game)
            #sleep(2)
        else: 
            streak - 0
            o += 1
           
            
        if streak > max_streak:
            max_streak = streak

        
    except TIE:
        t += 1


print (f"\n\n\n\nThe DummAI has won {o} times\nThe HorseAI has won {x} times\nand there has been {t} ties\nMax Horse Streak was {max_streak} wins in a row\n\n{x+o+t} matches were played\n")