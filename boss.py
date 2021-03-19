import config
from time import sleep


class Boss:
    def __init__(self):
        self.width = config.BOSS_WIDTH
        self.strength = config.BOSS_INITIAL_HEALTH
        self.shape = config.BOSS_SHAPE
        self.x = config.BOSS_INIT_POSITION[0]
        self.y = config.BOSS_INIT_POSITION[1]
        self.velX = config.BOSS_VEL

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

    def handleCollision(self, brick_array):
        self.strength -= 1
        if self.strength == 4:
            print("Boss is getting his defense layer ready")
            sleep(1)
            from levels.boss_level import createDefenseLayer
            createDefenseLayer(brick_array)
        if self.strength == 2:
            print("Boss is getting his 2nd defense layer ready")
            sleep(1)
            from levels.boss_level import createDefenseLayer2
            createDefenseLayer2(brick_array)
        if self.strength == 0:
            return True
        else:
            return False