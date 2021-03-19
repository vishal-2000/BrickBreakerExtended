from boss import Boss
import config
from queue import Queue
from miscellaneous import gameWon

class Bullet:
    def __init__(self, x, y):
        self.alive = True # if false the ball is no longer in use (it's dead)
        self.shape = config.BULLET_SHAPE
        self.width = config.BULLET_WIDTH
        self.velX = 0 # velocity (direction included) of ball in terms no of frames per move in x dir
        self.velY = -1 * config.FRAME_RATE # velocity of ball in terms no of frames per move in y dir
        self.x = x
        self.y = y
        self.__frameCount = 0 # frame count (a private variable) used for speed calculation and control
        self.type = "BULLET"

    def moveBulletAndBomb(self):
        if self.alive == False:
            return
        if self.velY !=0:
            if abs(config.FRAME_RATE//self.velY)==0:
                print("Invalid velocity please check2 :", self.velY)
                exit(1)
            if config.FRAME_COUNT%abs(config.FRAME_RATE//self.velY) == 0:
                self.y = self.y + int(1*(abs(self.velY)//self.velY))

    def handleExplodingBrickCollision(self, brick_array, brick1, powerup_array):
        config.SCORE += brick1.strength * 10
        powerup = brick1.brickSmash(self.velX, self.velY)
        if powerup!=None:
            powerup_array.append(powerup)
        q = Queue()
        q.put(brick1)
        while not q.empty():
            bricki = q.get()
            for brick in brick_array:
                if brick.color == "NONE":
                    continue
                if( 
                    (brick.y == bricki.y and 
                    ((brick.x + config.BRICK_WIDTH == bricki.x) or (bricki.x + config.BRICK_WIDTH == brick.x)))
                    or
                    (((brick.y - 1 == bricki.y) or (brick.y + 1 == bricki.y)) and
                    (brick.x + config.BRICK_WIDTH >= bricki.x and brick.x <= bricki.x + config.BRICK_WIDTH))
                ):
                    if brick.color == "YELLOW" and brick.strength != 0:
                        #print('Hi --->')
                        q.put(brick)
                    config.SCORE += brick.strength * 10
                    powerup = brick.brickSmash(self.velX, self.velY)
                    if powerup!=None:
                        powerup_array.append(powerup)

    def checkBrickCollision(self, brick_array, powerup_array):
        horizontal_collision = False
        vertical_collision = False
        for brick in brick_array:
            if brick.color != "NONE":
                if brick.y == self.y and ((brick.x - self.width ==  self.x and self.velX > 0) or (brick.x + config.BRICK_WIDTH ==self.x and self.velX < 0)): # horizontal collision with the brick
                    horizontal_collision = True
                    # self.velX = -1 * self.velX
                    if brick.color == "YELLOW":
                        self.handleExplodingBrickCollision(brick_array, brick, powerup_array)
                    else:
                        powerup = brick.handleCollision(self.velX, self.velY) 
                        if powerup!=None:
                            powerup_array.append(powerup)
                        if brick.color != "WHITE":
                            config.SCORE += 10
                if ((brick.y - 1 == self.y and self.velY > 0) or (brick.y + 1 == self.y and self.velY < 0)) and (brick.x - self.width  <= self.x and brick.x + config.BRICK_WIDTH >= self.x): # the brick is above/below the ball
                    vertical_collision = True
                    #self.velY = -1 * self.velY
                    if brick.color == "YELLOW":
                        self.handleExplodingBrickCollision(brick_array, brick, powerup_array)
                    else:
                        powerup = brick.handleCollision(self.velX, self.velY)
                        if powerup!=None:
                            powerup_array.append(powerup)
                        if brick.color != "WHITE":
                            config.SCORE += 10
            else:
                continue
        if horizontal_collision == True:
            self.velX = 0
            self.alive = False
        if vertical_collision == True:
            self.velY = 0
            self.alive = False

    def checkBossCollision(self, boss, brick_array):
        if boss == None:
            return
        #print(self.y, boss.y)
        #sleep(0.2)
        game_over = False
        if self.y == boss.y + 1: # ball collides the downside of the boss
            #print("Collision")
            #sleep(1)
            if (self.x < (boss.x + boss.width)) and (self.x > boss.x-self.width) and self.velY < 0:
                self.velY = 0
                self.alive = False
                #print("Collision")
                #sleep(1)
                game_over = boss.handleCollision(brick_array)
            if game_over == True:
                gameWon()
        if self.y == boss.y: # a case where the ball intersects the boss (error case)
            if (self.x < (boss.x + boss.width)) and self.x > boss.x-self.width:
                print('Invalid Ball and boss positioning')
                exit(1)
            if (self.x + self.width == boss.x and self.velX > 0) or (self.x == boss.x + boss.width or self.velX < 0):
                self.velX = 0
                if self.velY < 0:
                    self.velY = 0
                    self.alive = False
                game_over = boss.handleCollision(brick_array)
            if self.x + self.width == boss.x or self.x == boss.x + boss.width:
                self.y = boss.y + 1
                
        if game_over == True:
            gameWon()

    def checkCollision(self, brick_array, powerup_array, boss):
        if self.alive == False:
            return
        game_over = False
        # check brick collision
        self.checkBrickCollision(brick_array, powerup_array)
        self.checkBossCollision(boss, brick_array)
        # check frame collision
        
        if self.y == 1 and self.velY < 0:
            self.velY = 0
            self.alive = False
        
        