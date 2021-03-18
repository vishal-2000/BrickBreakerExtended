# Level 1 brick map
# This map creates and returns brick object array
from config import BRICK_WIDTH, FRAME_HEIGHT, FRAME_WIDTH, BOTTOM_EMPTY_SPACE
from brick import RedBrick, BlueBrick, GreenBrick, WhiteBrick, ExplodingBrick
from powerup import PowerUp, EpPowerUp, SpPowerUp, BmPowerUp, FbPowerUp, TbPowerUp, PgPowerUp
# Organization 
# layer 7 b g r b b r g b
# layer 6   r b g g b r
# layer 5     r w g b 
# layer 4       b g
# layer 3 y g g g y g g g
# layer 2 g y b y y y r b 
# layer 1 b w y r r r y r

def createMapLevel1(brick_array, powerup_array):
    # Creating bricks and their respective powerups
    # layer 7
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 4))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 4))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 4))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 4))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 4))
    # layer 6
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 5))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 5))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 5, BmPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 5)))
    # layer 5
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 6, FbPowerUp((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 6)))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 6))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6, TbPowerUp((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6)))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 6, PgPowerUp((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 6)))
    # layer 4
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 7, SpPowerUp((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 7)))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7, EpPowerUp((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7))) # powerup added
    #powerup_array.append(EpPowerUp((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7))
    # layer 3
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 8))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 8))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 8))
    # layer 2
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 9))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 9))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 9))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 9))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 9))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 9))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 9))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 9))
    # layer 1
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 10))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 10))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 10))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 10))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 10))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 10))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 10))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 10))