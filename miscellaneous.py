import config
from time import sleep
from os import system

def gameOver():
    print('G A M E O V E R')
    sleep(1)
    system('setterm -cursor on')
    exit(1)
def ballDead():
    config.NO_OF_LIVES -= 1
    if config.NO_OF_LIVES <= 0:
        gameOver()
    else:
        sleep(1)
def gameWon():
    print('Congratulations! You have completed the game the above game box shows your final score')
    print('Hope you have enjoyed, thank you!')
    sleep(2)
    system('setterm -cursor on')
    exit(1)