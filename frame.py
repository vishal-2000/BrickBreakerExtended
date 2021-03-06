# Created by Vishal Reddy Mandadi (started working on Feb 12 at 11:35pm)
# Used to generate game display frames
from powerup import ShPPowerUp
import config
import paddle
from colorama import Fore
from time import time
class Frame:
    def __init__(self, width, height):
        self.width = config.FRAME_WIDTH
        self.height = config.FRAME_HEIGHT
        self.score_height = config.SCORE_BOX_HEIGHT
        self.matrix = [[' ' for i in range(self.width)] for j in range(self.height)] # printing gamebox
        self.score_matrix = [[' ' for i in range(self.width)] for j in range(self.score_height)] # for printing score and player info
        
        # setting broder of the frame
        for i in range(self.width):
            self.matrix[0][i] = '-'
            self.matrix[self.height-1][i] = '-'
        for i in range(self.height):
            self.matrix[i][0] = '|'
            self.matrix[i][self.width-1] = '|'

    def reset(self):
        self.width = config.FRAME_WIDTH
        self.height = config.FRAME_HEIGHT
        self.score_height = config.SCORE_BOX_HEIGHT
        self.matrix = None
        self.score_matrix = None
        self.matrix = [[' ' for i in range(self.width)] for j in range(self.height)] # printing gamebox
        self.score_matrix = [[' ' for i in range(self.width)] for j in range(self.score_height)] # for printing score and player info
        
        # setting broder of the frame
        for i in range(self.width):
            self.matrix[0][i] = '-'
            self.matrix[self.height-1][i] = '-'
        for i in range(self.height):
            self.matrix[i][0] = '|'
            self.matrix[i][self.width-1] = '|'

    def setScoreBox(self, ball1, powerup_array, boss):
        config.FRAME_COUNT += 1
        config.FRAME_COUNT_PER_LEVEL += 1
        current_time = time()
        time_elapsed = current_time - config.START_TIME
        for i in range(config.SCORE_BOX_HEIGHT):
            for j in range(config.FRAME_WIDTH):
                if j == 0 or j==config.FRAME_WIDTH - 1:
                    self.score_matrix[i][j] = '|'
                elif i==0 or i==config.SCORE_BOX_HEIGHT-1:
                    self.score_matrix[i][j] = '-'
                else:
                    self.score_matrix[i][j] = ' '
        scoreString = 'Score: ' + str(config.SCORE)
        penaltyString = 'Penalty: ' + str(int(config.PENALTY))
        config.TOTAL_SCORE = config.SCORE - int(config.PENALTY)
        totalScoreString = 'Total Score: ' + str(config.TOTAL_SCORE)
        lifeCountString = 'Available Lives: ' + str(config.NO_OF_LIVES)
        velXString = 'Velocity of ball (Horizontal): ' + str(ball1.velX)
        velYString = 'Velocity of ball (Vertical): ' + str(ball1.velY)
        frameCountString = 'Frame count: ' + str(config.FRAME_COUNT)
        timeElapsedString = 'Time elapsed(in S): ' + str(round(time_elapsed, 2))
        ShP_powerupRemainingTime = 'ShP Remaining time: NA'
        if boss != None:
            bossHealth = 'Boss Health: ' + ('|'*boss.strength) + ('*'*(config.BOSS_INITIAL_HEALTH - boss.strength))
        else:
            bossHealth = 'Boss Health: ' + 'NA'
        for i in powerup_array:
            if i.type=="ShP" and i.active == True:
                ShP_powerupRemainingTime = 'ShP Remaining time: ' + str(config.POWERUP_TIMEPERIOD - time() + i.start_time)
        for i in range(len(config.GAME_NAME)):
            self.score_matrix[1][(config.FRAME_WIDTH - len(config.GAME_NAME))//2 + i] = config.GAME_NAME[i]
        for i in range(len(scoreString)):
            self.score_matrix[2][i+1] = scoreString[i]
        for i in range(len(lifeCountString)):
            self.score_matrix[2][config.FRAME_WIDTH - 2 - len(lifeCountString) + i] = lifeCountString[i]
        for i in range(len(penaltyString)):
            self.score_matrix[3][i+1] = penaltyString[i]
        for i in range(len(totalScoreString)):
            self.score_matrix[3][config.FRAME_WIDTH - 2 - len(totalScoreString) + i] = totalScoreString[i]
        for i in range(len(velXString)):
            self.score_matrix[4][i+1] = velXString[i]
        for i in range(len(frameCountString)):
            self.score_matrix[4][config.FRAME_WIDTH - 2 - len(frameCountString) + i] = frameCountString[i]
        for i in range(len(velYString)):
            self.score_matrix[5][i+1] = velYString[i]
        for i in range(len(timeElapsedString)):
            self.score_matrix[5][config.FRAME_WIDTH - 2 - len(timeElapsedString) + i] = timeElapsedString[i]
        for i in range(len(ShP_powerupRemainingTime)):
            self.score_matrix[6][i+1] = ShP_powerupRemainingTime[i]
        for i in range(len(bossHealth)):
            self.score_matrix[6][config.FRAME_WIDTH - 2 - len(bossHealth) + i] = bossHealth[i]

    def setBoard(self, ball_array, powerup_array, bullet_array):
        for i in range(1, self.width-1):
            self.matrix[config.FRAME_HEIGHT - config.BOTTOM_EMPTY_SPACE][i] = ' '
            self.matrix[1][i] = ' ' # Clearing boss positions
        for balli in ball_array:
            for i in range(config.BALL_WIDTH):
                if balli.y < 1 or balli.x > config.FRAME_WIDTH - 2:
                    if balli.alive == True:
                        print("Invalid ball position 1")
                        exit(1)
                else:
                    if balli.alive == True:
                        self.matrix[balli.y][balli.x + i] = ' '
        for bullet in bullet_array:
            for i in range(config.BULLET_WIDTH):
                if bullet.y < 1 or bullet.x > config.FRAME_WIDTH - 2:
                    if bullet.alive == True:
                        print("Invalid bullet position 1")
                        exit(1)
                else:
                    if bullet.alive == True:
                        self.matrix[bullet.y][bullet.x + i] = ' '

        for powerup in powerup_array:
            if powerup.appear == False:
                continue
            else:
                for j in range(config.POWERUP_WIDTH):
                    self.matrix[powerup.y][powerup.x + j] = ' '
        #for i in range(self.width):
        #    self.matrix[0][i] = '-'
        #    self.matrix[self.height-1][i] = '-'
        #for i in range(self.height):
        #    self.matrix[i][0] = '|'
        #    self.matrix[i][self.width-1] = '|'

    def setPaddle(self, paddle1):
        #self.setBoard()
        for i in range(paddle1.width):
            self.matrix[config.FRAME_HEIGHT - config.BOTTOM_EMPTY_SPACE][paddle1.x + i] = paddle1.shape[i]

    def setBoss(self, boss1):
        #self.setBoard()
        if boss1 == None:
            return
        for i in range(boss1.width):
            self.matrix[boss1.y][boss1.x + i] = boss1.shape[i]

    def setBall(self, ball_array):
        #self.setBoard()
        for balli in ball_array:
            if balli.alive == True:
                for i in range(balli.width):
                    if balli.alive == False:
                        continue
                    if balli.y < 1 or balli.x + i > config.FRAME_WIDTH - 2:
                        print("Invalid ball position 2")
                        exit(1)
                    self.matrix[balli.y][balli.x + i] = balli.shape[i]

    def setBullet(self, bullet_array):
        for bullet in bullet_array:
            if bullet.alive == True:
                for i in range(config.BULLET_WIDTH):
                    if bullet.alive == False:
                        continue
                    if bullet.y < 1 or bullet.x + i > config.FRAME_WIDTH - 2:
                        print("Invalid bullet position 2")
                        exit(1)
                    self.matrix[bullet.y][bullet.x + i] = bullet.shape[i]

    def setPowerUp(self, powerup_array):
        for powerup in powerup_array:
            if powerup.appear == True:
                for i in range(len(powerup.shape)):
                    self.matrix[powerup.y][powerup.x + i] = powerup.shape[i]

    def printFrame(self, brick_array, ball_array, powerup_array, boss):

        # time elapsed and frame count will be set by setScoreBox function
        # calculating penalty
        config.PENALTY = int(config.FRAME_COUNT//config.FRAME_RATE)
        # Printing Score Box
        self.setScoreBox(ball_array[0], powerup_array, boss)
        for i in range(config.SCORE_BOX_HEIGHT):
            for j in range(config.FRAME_WIDTH):
                print(self.score_matrix[i][j], end='')
            print('')
        # Printing Game Box
        brick_iterator = 0 # implies the iterator is at first brick
        for i in range(self.height):
            count = 0
            for j in range(self.width):
                if j < count:
                    continue
                if brick_iterator < len(brick_array):
                    if i == brick_array[brick_iterator].y:
                        if j == brick_array[brick_iterator].x:
                            for k in range(config.BRICK_WIDTH):
                                if brick_array[brick_iterator].color == "RED":
                                    print(Fore.RED + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "BLUE":
                                    print(Fore.BLUE + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "GREEN":
                                    print(Fore.GREEN + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "YELLOW":
                                    print(Fore.YELLOW + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "WHITE":
                                    print(Fore.WHITE + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "NONE":  # Indicates broken brick
                                        print(Fore.WHITE + self.matrix[i][j+k], end ="")
                            count = j + config.BRICK_WIDTH
                            brick_iterator += 1
                        else:
                            print(Fore.WHITE + self.matrix[i][j], end ="")
                    else:
                        print(Fore.WHITE + self.matrix[i][j], end ="")
                else:
                    print(Fore.WHITE + self.matrix[i][j], end ="")
            print('')        