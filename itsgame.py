import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))
    
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

n = 0
k = 0
s = 0
q = 0

def new_ball():
    '''
    draw new ball
    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    '''
    fun prints coordinates of point of the center ball and point of click
    and says it's inside or outside
    event - show coordinates of points
    '''
    global n, k, s, q
    '''print(x, y, r)
    print(event.pos)'''
    if (x - event.pos[0])**2 + (y - event.pos[1])**2 <= r**2:
        print('Got')
        n+=1
        k+=1
        s+= ((x - event.pos[0])**2 + (y - event.pos[1])**2) / r**2
        q+=1
    else:
        print('Miss')
        k+=1
        q+=1
        

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if k != 0:
                    print('Accuracy: ', n/k * 100,'%')
                    n, k = 0, 0
                else:
                    print("You haven't shoot yet")
            elif event.key == pygame.K_s:
                if q != 0:
                    print('Score:', s/q * 1000)
                    q, s = 0, 0
                else:
                    print("You haven't shoot yet to get score")
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
