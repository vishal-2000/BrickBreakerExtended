import config

class Brick:
    def __init__(self, strength, x, y, powerup_associated):
        self.x = x
        self.y = y
        self.shape = config.BRICK_SHAPE
        self.width = config.BRICK_WIDTH
        self.strength = strength
        self.color = ""
        self.broken = "NO" # implies the brick is not broken yet
        self.powerup_associated = powerup_associated
        self.type = "NORMAL"

    def positionUpdate(self):
        if 1: #self.color != "NONE":
            if config.FRAME_COUNT_PER_LEVEL > config.FALLING_BRICK_FRAME_NUMBER:
                self.y = self.y + 1
                if self.y >= config.PADDLE_INITIAL_POS[1]:
                    from miscellaneous import gameOver
                    gameOver()

    def colorChange(self): # used to decrease color on collision
        if self.color == "RED": 
            self.color = "BLUE"
        elif self.color == "BLUE":
            self.color = "GREEN"
        elif self.color == "GREEN" or self.color == "YELLOW":
            self.color = "NONE" # implies the brick is broken
            #self.x = 0
            #self.y = 0

    def handleCollision(self):
        if self.color == "WHITE" or self.color == "NONE":
            return
        if self.color == "GREEN" or self.color == "YELLOW":
            self.color = "NONE"
            self.broken = "YES"
            if self.powerup_associated!=None:
                (self.powerup_associated).releasePowerUp()
                return self.powerup_associated
        elif self.color == "BLUE":
            self.color = "GREEN"
        elif self.color == "RED":
            self.color = "BLUE"
        self.strength -= 1
    def brickSmash(self): # used in case of thru ball
        if self.color == "NONE":
            return None
        self.color = "NONE"
        self.broken = "YES"
        self.strength = 0
        if self.powerup_associated!=None:
                (self.powerup_associated).releasePowerUp()
                return self.powerup_associated


class RedBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, 3, x, y, powerup_associated) # strength = 3 # no of collisions required to break the brick
        self.color = "RED"

class BlueBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, 2, x, y, powerup_associated) # strength = 3 # no of collisions required to break the brick
        self.color = "BLUE"

class GreenBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, 1, x, y, powerup_associated) # strength = 3 # no of collisions required to break the brick
        self.color = "GREEN"

class WhiteBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, -1, x, y, powerup_associated) # strength = 3 # no of collisions required to break the brick
        self.color = "WHITE"

class ExplodingBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, 1, x, y, powerup_associated)
        self.color = "YELLOW"

class RainbowBrick(Brick):
    def __init__(self, x, y, powerup_associated = None):
        Brick.__init__(self, 3, x, y, powerup_associated)
        self.color = "RED"
        self.type = "RAINBOW" # type changes to normal the moment the block gets hit by the ball

    def handleCollision(self):
        self.type = "NORMAL"
        return super().handleCollision()

    def changeColor(self):
        if self.type != "RAINBOW" or config.FRAME_COUNT%config.RAINBOW_COLOR_CHANGE_RATE != 0:
            return

        if self.color == "RED":
            self.color = "BLUE"
            self.strength = 2
            return
        if self.color == "BLUE":
            self.color = "GREEN"
            self.strength = 1
            return
        if self.color == "GREEN":
            self.color = "RED"
            self.strength = 3
            return