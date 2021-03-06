# Level 1 brick map
# This map creates and returns brick object array
from config import BRICK_WIDTH, FRAME_HEIGHT, FRAME_WIDTH, BOTTOM_EMPTY_SPACE
from brick import RedBrick, BlueBrick, GreenBrick, WhiteBrick, ExplodingBrick, RainbowBrick
from powerup import PowerUp, EpPowerUp, SpPowerUp, BmPowerUp, FbPowerUp, TbPowerUp, PgPowerUp, ShPPowerUp
# Organization 
# layer 7       b b   
# layer 6     g y y g 
# layer 5   b r y y r b
# layer 4 g g r y y r g g
# layer 3   g g b b g g
# layer 2     c g g c
# layer 1       w w
# here c implies rainbow colored brick
# g - green, r - red, b - blue, y - exploding yellow brick

def createMapLevel2(brick_array, powerup_array):
    # Creating bricks and their respective powerups
    # layer 7
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 4))
    # layer 6
    
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 5))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 5))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5, BmPowerUp((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5)))
    # layer 5
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 6, FbPowerUp((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 6)))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 6))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 6))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6, TbPowerUp((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6)))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 6))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 6, PgPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 6)))
    # layer 4
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 7))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 7, SpPowerUp((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 7)))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 7))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 7))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 7))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 7, EpPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 7)))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 7))

    # layer 3
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 8))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 8))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 8, ShPPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 8)))
    # layer 2
    brick_array.append(RainbowBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 9))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 9))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 9))
    brick_array.append(RainbowBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 9))
    # layer 1
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 10))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 10))
    