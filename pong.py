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
def drawPaddle(PaddleXPos):
    #create a bar for paddle
    paddle = pygame.Rect()


