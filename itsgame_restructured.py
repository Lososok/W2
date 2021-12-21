import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 800))
    
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
quantity = 3
p = []
score = 0
for i in range(quantity):
    p.append([])
    
def click(event, c):
    global score
    n = 0
    for i in range(quantity):
        x = p[i][0]
        y = p[i][1]
        r = p[i][2]
        if (x - event.pos[0])**2 + (y - event.pos[1])**2 <= r**2:
            print('Got')
            n += 1
            score += 100
    if n == 0:
        print('Miss')
        print('Score:', score)
        score = 0
    
def draw_ball(c):
    x = c[0]
    y = c[1]
    r = c[2]
    color = c[3]
    circle(screen, color, (x, y), r)

def xyr():
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(25, 100)
    color = COLORS[randint(0, 5)]
    return x, y, r, color

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, p[i])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if k != 0:
                    print('Accuracy: ', n/k * 100,'%')
                    n, k = 0, 0
                else:
                    print("You haven't shoot yet")
            elif event.key == pygame.K_s:
                print('Score:', score)
                score = 0
    for i in range(quantity):
        p[i] = xyr()
        draw_ball(p[i]) 
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
