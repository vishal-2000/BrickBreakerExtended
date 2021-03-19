# Assignment3_SSAD
Extension of Assignment 2
The Brick Breaker Game using python3 and OOPS concepts (DASS course assignment (14th to 17th Feb))
## Creator information
- Created by Vishal Reddy Mandadi 
- DASS Course assignment 2

## New Features (Through Assignment 3)
### Controls
- 's' to skip the current level and go to the next level
### Levels
- There are three levels to choose from or you could also play all sequentially:
    - Level 1 == ordinary level
    - Level 2 == ordinary level
    - Level 3 == Boss Level 
- You can choose a level directly from the start screen. Then you can start playing it. The remaining lives will remain constant accross the levels (it won't change on simply upgrading the level)

### Falling Bricks
- In each level, you will be given 100 frames time. After crossing 100th frame, the bricks will drif downward every time your ball hits your paddle
- The moment a brick comes close enough to your paddle in such a way that paddle's locomotive freedom is restricted, then the game ends. It is a GAMEOVER scenario

### Rainbow bricks
- These bricks keep changing their colors at certain rate. They stop changing colors as soon as they are hit by the ball

### Powerups 2.0
- Acceleration due to gravity added
- The powerups initial velocity will be same as that of the ball when it hits the brick

## How to run the game
### Dependencies
- Python 3
- Numpy
### Run instructions
- Download the zip file from github or moodle
- Extract all files
- Enter 'python3 main.py' command in the terminal (or in simple terms just execute the main.py file)

## Game objectives
- Break as many bricks as possible in as much less time as possible
- The game ends when all bricks are broken or when all lives are lost
- Objective should be to maximize the total score

## Controls
- 'a' to move the paddle left
- 'd' to move the paddle right
- ' ' or spacebar to release the ball from the paddle
- 's' to skip the current level and go to the next level
## Score
- Each collision with a breakable brick awards 10 points
- A penalty of 1 point is incurred after every 24 frames (Frame rate is 24 frames/sec)
- The total score = (no of breakable brick collisions) - (no of frames until end of the game / 24)

## Ball
- The ball initially has only vertical velocity
- If the ball hit's the bottom of the game box, it will be dead (will disappear)
- The x velocity of the ball increases or decreases depending on the position where it hits the paddle 

## Lives
- You will be given 3 lives
- No penalty incurred if you lose a life
- When you lose your life, all the active powerups will be deactivated
- You will lose a life if all the balls are dead

## Bricks
- White bricks are unbreakable
- Red bricks will break after 3 collisions
- Blue bricks will break after 2 collisions
- Green bricks will break after 1 collision
- Yellow bricks called exploding bricks break after 1 collision and break all the bricks adjacent or diagonal to them
- Rainbow bricks - These bricks keep changing their colors at certain rate. They stop changing colors as soon as they are hit by the ball (strength will also change in accordance with the color)

## Powerups
Catch the powerups with the paddle to activate them (they are hidden in the breaks and start falling down once the corresponding bricks are broken)
- '$EP$' - expands the paddle
- '$SP$' - Shrinks the paddle
- '$PG$' - Paddle grab (The ball will be grabbed by the paddle on collision with it, it can be released by clicking the spacebar)
- '$BM$' - Ball multiplier (Introduces an extraball into the game which starts from a certain initial position)
- '$FB$' - Fast Ball (Increases the speed of the ball)
- '$TB$' - Through Ball (The ball can go undeflected by the bricks and all those bricks which come into contact will be smashed (including the unbreakable type))
### Note:
- More than two powerups can be active at a time
- if EP and SP are both activated, the one which is caught later will be acitive (I implemented this only in this case (will change it if the TA insists))

## Bonus Implemented!
- The yellow colored bricks are called exploding bricks
- They appear in packs of size more than 6
- On collision all the adjacent and diagonal bricks break
- The exploding bricks even break the unbreakable ones
