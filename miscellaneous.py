from boss import Boss
import config
from time import sleep
from os import system

#

def gameOver():
    #system('clear')
    #frame1.printFrame(brick_array, ball_array, powerup_array, boss)
    print('G A M E O V E R')
    sleep(1)
    system('setterm -cursor on')
    exit(1)
def ballDead(level = None, ball_array = None, powerup_array = None, brick_array = None, bullet_array = None, boss = None, paddle1 = None, frame1 = None):
    system('clear')
    config.NO_OF_LIVES -= 1
    if frame1 != None:
        frame1.printFrame(brick_array, ball_array, powerup_array, boss)
    if config.NO_OF_LIVES <= 0:
        gameOver()
    else:
        sleep(1)

def levelWon(level = None, ball_array = None, powerup_array = None, brick_array = None, bullet_array = None, boss = None, paddle1 = None, frame1 = None):
    config.FRAME_COUNT_PER_LEVEL = 0
    system('clear')
    if frame1 != None:
        frame1.printFrame(brick_array, ball_array, powerup_array, boss)
    print('Congratulations! Level {:d} is complete'.format(level))
    if level >= 1 and level < 3:
        print('Promoting you to level {:d}'.format(level+1))
        level, ball_array, powerup_array, brick_array, bullet_array, boss = levelUp(level, ball_array, powerup_array, brick_array, bullet_array, boss, paddle1, frame1)
        sleep(2)
        return level, ball_array, powerup_array, brick_array, bullet_array, boss
    elif level == 3:
        gameWon()

def levelUp(level, ball_array, powerup_array, brick_array, bullet_array, boss, paddle1, frame1):
    from levels.level1 import createMapLevel1
    from levels.level2 import createMapLevel2
    from levels.boss_level import createMapLevel3
    config.FRAME_COUNT_PER_LEVEL = 0
    for powerup in powerup_array:
        powerup.deactivatePowerUp(paddle1, ball_array)
    #ball_array = None
    ball_array = []
    bullet_array = []
    from ball import Ball
    ball_array.append(Ball())
    paddle1.x = config.PADDLE_INITIAL_POS[0]
    paddle1.y = config.PADDLE_INITIAL_POS[1]
    #powerup_array = None
    #brick_array = None
    powerup_array = []
    brick_array = []
    boss = None
    if level == 1:
        print("Moving to level 2 from level 1, Please wait ...\n")
        createMapLevel2(brick_array, powerup_array)
    elif level == 2:
        print("Moving to level 3 from level 2, Please wait ...\n")
        boss = createMapLevel3(brick_array, powerup_array)
    elif level == 3:
        print("Cannot promote from level 3, game over. Thanks\n")
        gameOver()
        #createMapLevel2(brick_array, powerup_array)
    level += 1
    sleep(1)
    frame1.reset()
    frame1.setBoard(ball_array, powerup_array, bullet_array)
    frame1.setPaddle(paddle1)
    frame1.setBall(ball_array)
    frame1.setBullet(bullet_array)
    frame1.setPowerUp(powerup_array)
    return level, ball_array, powerup_array, brick_array, bullet_array, boss
    
def gameWon():
    #system('clear')
    #frame1.printFrame(brick_array, ball_array, powerup_array, boss)
    print('Congratulations! You have completed the game the above game box shows your final score')
    print('Hope you have enjoyed, thank you!')
    sleep(2)
    system('setterm -cursor on')
    exit(1)