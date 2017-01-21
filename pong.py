import pygame
import random

#frame rate per second
FPS = 60

#size of the window
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 400

#size of paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#distance from the edge of window
PADDLE_BUFFER = 10

#size of the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#speed of paddle and ball
PADDLE_SPEED = 2
BALL_X_SPEED = 2
BALL_Y_SPEED = 2

#RGB co;ours of paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#initialise our screen using width and height vars
screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

#draw the ball
def drawBall(ballXPos, ballYPos):
    #create a small rectangle
    ball = pygame.Rect(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.rect(screen, WHITE, ball)

#draw paddle
def drawPaddle(paddleXPos, paddleYPos):
    #create a bar for paddle
    paddle = pygame.Rect(paddleXPos, paddleYPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle)

# update the ball, using the paddle positions, teh ball positions and the balls direction
def updateBall(paddleXPos, ballXPos, ballYPos, ballXDirection, ballYDirection):

    #update x and y position for ball
    ballXPos = ballXPos + ballXDirection * BALL_X_SPEED
    ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED
    score = 0

    #check for the collistion on the paddle
    if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballXPos + BALL_HEIGHT >= paddleXPos and ballXPos + BALL_HEIGHT <= paddleXPos + PADDLE_HEIGHT):
        #switch the direction
        ballXDirection = 1
    elif (ballXDirection <= 0):
        #negative score
        ballXDirection = 1
        score = -1
        return [score, paddleXPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

    #if it hits the top, then move down
    if (ballYPos <= 0):
        ballYPos = 0;
        ballYDirection = 1;
    #if it hits the bottom, then move up
    elif (ballYPos >= WINDOW_HEIGHT - BALL_HEIGHT):
        ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1

    return [score, paddleXPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

    #update the paddle position

def updatePaddle(action, paddleXPos):
    #if move up
    if(action[1] == 1):
        paddleYPos = paddleXPos - PADDLE_SPEED
    #if move down
    if (action[2] == 1):
        paddleYPos = paddleXPos + PADDLE_SPEED

    # don't let move out of the screen
    if(paddleXPos < 0):
        paddleXPos = 0
    if(paddleXPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddleXPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddleYPos

#game class
class PongGame:
    def __init__(self):
        #random number for initial direction of ball
        #keep score
        self.tally = 0
        #initialie position of paddle
        self.paddleYPos = WINDOW_HEIGHT / 2 -PADDLE_HEIGHT /2
        #ball direction
        self.ballXDirection = 1
        self.ballYDirection = 1
        #restarting point
        self.ballXPos = WINDOW_WIDTH / 2 - BALL_WIDTH / 2

        #randomly decide where the ball will move
        if(0 < num < 3 ):
            self.ballXDirection = 1
            self.ballYDirection = 1
        if(3 <= num < 5):
            self.ballXDirection = -1
            self.ballYDirection = 1
        if(5 <= num < 8):
            self.ballXDirection = 1
            self.ballYDirection = -1
        if(8 <= num < 10):
            self.ballXDirection = -1
            self.ballYDirection = -1

        #new random number
        num = random.randInt(0,9)
        #where it will start, y part
        self.ballYPos = num * (WINDOW_HEIGHT - BALL_HEIGHT)/9

    def getPresentFrame(self):
        #for each frame, calls the event queue, like if the main window needs to be repainted
        pygame.event.pump()
        #make the background back
        screen.fill(BLACK)
        #draw our paddles
        drawPaddle(self.paddleYPos)
        #draw the ball
        drawBall(self.ballXPos, self.ballYPos)
        #copy the pixel from our surface to a 3D array. we'll use this for RL
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update the window
        pygame.display.flip()
        #return our surface data
        return image_data

    #update our screen
    def getNextFrame(self, action):
        pygame.event.pump()
        score = 0
        screen.fill(BLACK)
        #update our paddle
        self.paddleYPos = updatePaddle(action, self.paddleYPos)
        drawPaddle(self.paddleYPos)
        #update our vars by uodating ball position
        [score, self.ballXDirection, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYPos, self.ballXDirection, self.ballYDirection] = updateBall(self.paddleYPos, self.paddleXpos, self.ballXDirection, self.ballYDirection)
        #draw the ball
        drawBall(self.ballXPos, self.ballYPos)
        #get the surface data
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update the window
        pygame.display.flip()
        #record the total score
        self.tally = self.tally + score
        print "Tally is " + str(self.tally)
        #return the score and the surface data
        return[score, image_data]

