# Created by Vishal Reddy Mandadi
from levels.level1 import createMapLevel1
from levels.level2 import createMapLevel2
from levels.boss_level import createMapLevel3

import config
from paddle import Paddle
from ball import Ball
from frame import Frame
from os import system
from time import sleep, time
import input_template
from miscellaneous import ballDead, gameOver, gameWon, levelUp, levelWon


config.START_TIME = time() # in seconds
# initialize objects of the game
paddle1 = Paddle()
ball_array = [ Ball() ] # initially contains single ball
frame1 = Frame(config.FRAME_WIDTH, config.FRAME_HEIGHT)
get_object = input_template.Get()
brick_array = []
powerup_array = []

system('clear')

level = int(input("Choose a level from 1-3: "))

while(1):
    #print(level)
    if level == 1:
        createMapLevel1(brick_array, powerup_array)
        break
    elif level == 2:
        createMapLevel2(brick_array, powerup_array)
        break
    elif level == 3:
        createMapLevel3(brick_array, powerup_array)
        break
    else:
        print("\n")
        level = int(input("Invalid input, Please input a valid level from 1, 2 and 3: "))


#paddle1.printPaddle()

# rendering at FRAME_RATE frames per second
frame1.setBoard(ball_array, powerup_array)
frame1.setPaddle(paddle1)
frame1.setBall(ball_array)
frame1.setPowerUp(powerup_array)
frame1.printFrame(brick_array, ball_array)

# switching off the cursor
system('setterm -cursor off')

# Handling input and main game loop
while(1):
    #sleep(2/config.FRAME_RATE)
    c = input_template.input_to(get_object, 2/config.FRAME_RATE) # here 2nd arguement mentions timeout (waiting time untill an input is recieved)
    system('clear')
    #system('setterm -cursor off')
    if c=='\x03':
        system('setterm -cursor on')
        break
    if c==' ':
        for ball1 in ball_array:
            ball1.releaseBall()
    elif c=='d':
        paddle1.moveRight()
    elif c=='a':
        paddle1.moveLeft()
    elif c=='s': # levelUp
        system('clear')
        system('setterm -cursor on')
        print("Jumping to the next level, Please wait ...\n")
        level, ball_array, powerup_array, brick_array = levelUp(level, ball_array, powerup_array, brick_array, paddle1, frame1)


    frame1.setBoard(ball_array, powerup_array) # erase the previous positions 
    for ball1 in ball_array:
        ball1.moveBall(c) # now move ball
    for i in powerup_array: # move powerup
        i.movePowerUp()
        i.checkCollision(paddle1, ball_array)
        if (time() - i.start_time) >= config.POWERUP_TIMEPERIOD and i.active == True:
            i.deactivatePowerUp(paddle1, ball_array)
    for ball1 in ball_array:
        game_over = ball1.checkCollision(paddle1, brick_array, powerup_array)
    game_over = True
    for ball1 in ball_array:
        if ball1.alive == True:
            game_over = False
            break

    for brick in brick_array:
        if brick.type == "RAINBOW":
            brick.changeColor()
    temp = 0
    for brick in brick_array:
        if brick.color!="NONE" and brick.color!="WHITE":
            temp += 1
            break
    if temp == 0:
        system('clear')
        frame1.printFrame(brick_array, ball_array)
        level, ball_array, powerup_array, brick_array = levelWon(level, ball_array, powerup_array, brick_array, paddle1, frame1)

    if game_over == True:
        system('clear')
        frame1.printFrame(brick_array, ball_array)
        ballDead()
        ball_array = []
        ball_array.append(Ball())
        paddle1.x = config.PADDLE_INITIAL_POS[0]
        paddle1.y = config.PADDLE_INITIAL_POS[1]
        # deactivate the active powerups
        for powerup in powerup_array:
            powerup.deactivatePowerUp(paddle1, ball_array)



    frame1.setPaddle(paddle1) # set paddle
    frame1.setBall(ball_array) # set ball
    frame1.setPowerUp(powerup_array)
    frame1.printFrame(brick_array, ball_array)


