# Level 1 brick map
# This map creates and returns brick object array
from config import BRICK_WIDTH, FRAME_HEIGHT, FRAME_WIDTH, BOTTOM_EMPTY_SPACE
from brick import RedBrick, BlueBrick, GreenBrick, WhiteBrick, ExplodingBrick, RainbowBrick
from powerup import PowerUp, EpPowerUp, SpPowerUp, BmPowerUp, FbPowerUp, TbPowerUp, PgPowerUp, ShPPowerUp
from boss import Boss
# Organization full health
# layer 8        boss
# layer 7         
# layer 6       g r r g 
# layer 5   r b w     w b r
# layer 4   w   y y y y   w
# layer 3   r b w     w b r
# layer 2       b c c b
# layer 1    
# here c implies rainbow colored brick
# g - green, r - red, b - blue, y - exploding yellow brick  

def createMapLevel3(brick_array, powerup_array):
    # Creating bricks and their respective powerups
    # layer 8
    
    boss = Boss()

    # layer 7
    
    # layer 6
    
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 5))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 5))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5, BmPowerUp((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5)))
    # layer 5

    brick_array.append(RedBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 6))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 6, FbPowerUp((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 6)))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 6))
    #brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 6))
    #brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6, TbPowerUp((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6)))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 6))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 6, PgPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 6)))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 6, TbPowerUp((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 6)))
    # layer 4

    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 7))
    #brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 7, SpPowerUp((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 7)))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 7, SpPowerUp((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 7)))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 7))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7))
    brick_array.append(ExplodingBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 7, EpPowerUp((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 7)))
    #brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 7, EpPowerUp((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 7)))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 7))

    # layer 3
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 8))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 8))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 8))
    #brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 8))
    #brick_array.append(BlueBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 8))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 8))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 8))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 8, ShPPowerUp((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 8)))
    # layer 2
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 9))
    brick_array.append(RainbowBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 9))
    brick_array.append(RainbowBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 9))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 9))
    # layer 1
    #brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 10))
    #brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 10))

    return boss
    

# Organization full health
# layer 9         boss
# layer 8 c c c c c c c c c c       
# layer 7 c c c c c c c c c c        
# layer 6       g r r g 
# layer 5   r b w     w b r
# layer 4   w   y y y y   w
# layer 3   r b w     w b r
# layer 2       b c c b
# layer 1    
# here c implies rainbow colored brick
# g - green, r - red, b - blue, y - exploding yellow brick  


def createDefenseLayer(brick_array):
    # layer 7
    brick_array.insert(0, RainbowBrick((FRAME_WIDTH//2) - 8*BRICK_WIDTH, 4))
    brick_array.insert(1, RainbowBrick((FRAME_WIDTH//2) - 7*BRICK_WIDTH, 4))
    brick_array.insert(2, RainbowBrick((FRAME_WIDTH//2) - 6*BRICK_WIDTH, 4))
    brick_array.insert(3, RainbowBrick((FRAME_WIDTH//2) - 5*BRICK_WIDTH, 4))
    brick_array.insert(4, RainbowBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 4))
    brick_array.insert(5, RainbowBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 4))
    brick_array.insert(6, RainbowBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 4))
    brick_array.insert(7, RainbowBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 4))
    brick_array.insert(8, RainbowBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 4))
    brick_array.insert(9, RainbowBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 4))
    brick_array.insert(10, RainbowBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 4))
    brick_array.insert(11, RainbowBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 4))
    brick_array.insert(12, RainbowBrick((FRAME_WIDTH//2) + 4*BRICK_WIDTH, 4))
    brick_array.insert(13, RainbowBrick((FRAME_WIDTH//2) + 5*BRICK_WIDTH, 4))
    brick_array.insert(14, RainbowBrick((FRAME_WIDTH//2) + 6*BRICK_WIDTH, 4))
    brick_array.insert(15, RainbowBrick((FRAME_WIDTH//2) + 7*BRICK_WIDTH, 4))

def createDefenseLayer2(brick_array):
    # layer 8
    brick_array.insert(0, RainbowBrick((FRAME_WIDTH//2) - 8*BRICK_WIDTH, 3))
    brick_array.insert(1, RainbowBrick((FRAME_WIDTH//2) - 7*BRICK_WIDTH, 3))
    brick_array.insert(2, RainbowBrick((FRAME_WIDTH//2) - 6*BRICK_WIDTH, 3))
    brick_array.insert(3, RainbowBrick((FRAME_WIDTH//2) - 5*BRICK_WIDTH, 3))
    brick_array.insert(4, RainbowBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 3))
    brick_array.insert(5, RainbowBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 3))
    brick_array.insert(6, RainbowBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 3))
    brick_array.insert(7, RainbowBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 3))
    brick_array.insert(8, RainbowBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 3))
    brick_array.insert(9, RainbowBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 3))
    brick_array.insert(10, RainbowBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 3))
    brick_array.insert(11, RainbowBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 3))
    brick_array.insert(12, RainbowBrick((FRAME_WIDTH//2) + 4*BRICK_WIDTH, 3))
    brick_array.insert(13, RainbowBrick((FRAME_WIDTH//2) + 5*BRICK_WIDTH, 3))
    brick_array.insert(14, RainbowBrick((FRAME_WIDTH//2) + 6*BRICK_WIDTH, 3))
    brick_array.insert(15, RainbowBrick((FRAME_WIDTH//2) + 7*BRICK_WIDTH, 3))






# Organization 1 at health 4
# layer 8       boss
# layer 7 r   r   g g   r   r
# layer 6       w     w 
# layer 5   c             c   
# layer 4   w             w
# layer 3 c   c         c   c
# layer 2       w     w
# layer 1  

  

# Organization 1 at health 2
# layer 8       boss
# layer 7 c   c   c c   c   c
# layer 6       w     w 
# layer 5 c   c         c   c
# layer 4   w     c c     w
# layer 3 c   c         c   c
# layer 2       w     w
# layer 1      