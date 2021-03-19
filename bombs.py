from miscellaneous import ballDead, gameOver, gameWon
from bullets import Bullet
import config
from time import sleep

class Bomb(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = config.BOMB_SHAPE
        self.width = config.BOMB_WIDTH
        self.velY = -1 * self.velY
        self.type = "BOMB"

    def checkPaddleCollision(self, paddle1):
       
        game_over = False
        
        if self.y == paddle1.y - 1: # ball collides the downside of the boss
            #print("Collision")
            #sleep(1)
            if (self.x < (paddle1.x + paddle1.width)) and (self.x >= paddle1.x-self.width) and self.velY > 0:
                self.velY = 0
                self.alive = False
                ballDead()
        if self.y == paddle1.y: # a case where the ball intersects the boss (error case)
            if (self.x < (paddle1.x + paddle1.width)) and self.x > paddle1.x-self.width:
                print('Invalid Bomb and paddle positioning')
                exit(1)
            if (self.x + self.width == paddle1.x) or (self.x == paddle1.x + paddle1.width):
                self.velX = 0
                if self.velY > 0:
                    self.velY = 0
                    self.alive = False
                #game_over = boss.handleCollision(brick_array)
                ballDead()
                
        if game_over == True:
            gameWon()

    def checkCollision(self, brick_array, powerup_array, paddle1):
        #print("Hey")
        #sleep(1)
        if self.alive == False:
            return
        game_over = self.checkPaddleCollision(paddle1)
        if game_over == True:
            from miscellaneous import gameOver
            gameOver()
        if self.y == config.FRAME_HEIGHT - 2 and self.velY > 0:
            self.velY = 0
            self.alive = False
