import config
from time import time
from ball import Ball
class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.active = False
        self.appear = False # will be true when powerup is released until it's caught
        self.start_time = 0 # in sec
    def movePowerUp(self):
        if self.appear==False:
            return
        if self.velX !=0:
            #print('VelX = ',self.velX)
            if int(abs(config.FRAME_RATE//self.velX))==0:
                print("Invalid velocity please check1 :", self.velX)
                exit(1)
            if config.FRAME_COUNT%abs(int(config.FRAME_RATE//self.velX)) == 0:
                self.x = self.x + int(1*(abs(self.velX)//self.velX))
        if self.velY !=0:
            if abs(config.FRAME_RATE//self.velY)==0:
                print("Invalid velocity please check2 :", self.velY)
                exit(1)
            if config.FRAME_COUNT%abs(config.FRAME_RATE//self.velY) == 0:
                self.y = self.y + int(1*(abs(self.velY)//self.velY))
    def activatePowerUp(self, paddle1, ball1):
        self.velX = 0
        self.velY = 0
        self.active = True
        self.start_time = time()
        #print('Hey, I am here!')
    def deactivatePowerUp(self, paddle1, ball1):
        if self.active==False:
            return
        self.active = False
    def releasePowerUp(self):
        self.appear = True
        self.velX = config.POWERUP_VEL[0]
        self.velY = config.POWERUP_VEL[1]
    def checkCollision(self, paddle1, ball1):
        if self.appear==False:
            return
        if self.y == paddle1.y-1: # powerup collides the upside of the paddle
            if (self.x < (paddle1.x + paddle1.width)) and self.x > paddle1.x-config.POWERUP_WIDTH and self.velY > 0:
                # stop the power up
                self.velY = 0
                self.appear = False # dissapear the powerup
                self.activatePowerUp(paddle1, ball1)
        if self.y >= config.FRAME_HEIGHT - 2:
            # stop the power up
            self.velY = 0
            self.appear = False # dissapear the powerup
    def checkPowerUp(self):
        if self.appear == False:
            return

class EpPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.EP_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball1):
        paddle1.width = config.PADDLE_WIDTH + 2
        paddle1.shape = '|-------|'
        super().activatePowerUp(paddle1, ball1)
    def deactivatePowerUp(self, paddle1, ball1):
        paddle1.width = config.PADDLE_WIDTH
        paddle1.shape = config.PADDLE_SHAPE
        return super().deactivatePowerUp(paddle1, ball1)

class SpPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.SP_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball1):
        paddle1.width = config.PADDLE_WIDTH - 2
        paddle1.shape = '|---|'
        super().activatePowerUp(paddle1, ball1)
    def deactivatePowerUp(self, paddle1, ball1):
        paddle1.width = config.PADDLE_WIDTH
        paddle1.shape = config.PADDLE_SHAPE
        return super().deactivatePowerUp(paddle1, ball1)

class BmPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.BM_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball_array):
        ballx = Ball()
        ballx.velY = config.BALL_INIT_VEL[1]
        ballx.velX = config.BALL_INIT_VEL[0]
        ballx.ballGrabbed = False
        ball_array.append(ballx)
        super().activatePowerUp(paddle1, ball_array)
    def deactivatePowerUp(self, paddle1, ball_array):
        return super().deactivatePowerUp(paddle1, ball_array)

class FbPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.FB_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            if ball1.velY!=0:
                ball1.velY = (ball1.velY//abs(ball1.velY)) * abs(config.BALL_FAST_VEL[1])
        super().activatePowerUp(paddle1, ball_array)
    def deactivatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            if ball1.velY!=0:
                ball1.velY = (ball1.velY//abs(ball1.velY)) * abs(config.BALL_INIT_VEL[1])
        return super().deactivatePowerUp(paddle1, ball_array)

class TbPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.TB_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            ball1.thruBall = True
        super().activatePowerUp(paddle1, ball_array)
    def deactivatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            ball1.thruBall = False
        return super().deactivatePowerUp(paddle1, ball_array)

class PgPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.PG_POWERUP_SHAPE
    def activatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            ball1.ballWillBeGrabbed = True 
        #ball1.velX = 0
        #ball1.velY = 0
        super().activatePowerUp(paddle1, ball_array)
    def deactivatePowerUp(self, paddle1, ball_array):
        for ball1 in ball_array:
            ball1.ballWillBeGrabbed = False
        return super().deactivatePowerUp(paddle1, ball_array)

