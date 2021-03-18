import config
from time import sleep

class Paddle:
    def __init__(self):
        self.width = config.PADDLE_WIDTH
        self.height = config.PADDLE_HEIGHT
        self.x = config.PADDLE_INITIAL_POS[0]
        self.y = config.PADDLE_INITIAL_POS[1]
        self.shape = config.PADDLE_SHAPE

    def printPaddle(self):
        print('|'+'-'*(self.width-2) + '|')

    def moveRight(self):
        self.x = self.x + 1
        if self.x + self.width >= config.FRAME_WIDTH:
            #print('Invalid move')
            self.x = self.x - 1
            #sleep(2)

    def moveLeft(self):
        self.x = self.x - 1
        if self.x <= 0: 
            self.x = self.x + 1
    