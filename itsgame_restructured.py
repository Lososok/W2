import pygame
from pygame.draw import *
from random import randint, choice, random

pygame.init()

# global variables

FPS = 30
screen = pygame.display.set_mode((1200, 800))
    
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
quantity = 4
p = []
a = []
b = []
score = 0
for i in range(quantity):       
    p.append([])
    a.append(0)
    b.append(0)

def xyr():
    ''' creates random center (x, y), radius r, color color which add in tuple '''
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(25, 100)
    color = COLORS[randint(0, 5)]
    return x, y, r, color
    
def draw_ball(c):
    ''' draws ball with center (x, y), radius r and color color '''
    x = c[0]
    y = c[1]
    r = c[2]
    color = c[3]
    circle(screen, color, (x, y), r)

def draw_notball(c):                                                   # in work
    x = c[0]
    y = c[1]
    r = c[2]
    color = c[3]
    xr = r * round(random() * 2, 2)
    yr = r * round(random() * 2, 2) * 2/3
    ellipse(screen, color, ((x, y), (xr, yr)))

def move(c):
    '''
    responsible for the movement of all balls
    c - p[i] which save value of x, y, r and color
    '''
    global a, b, p
    x = p[i][0]
    y = p[i][1]
    r = p[i][2]
    speed = r * 0.125
    if  100 < x < 1100 and 100 < y < 700:       #ruls of motion. It's hardcode, I think
        if a[i] == 0 and b[i] == 0:
            a[i] = randint(-1, 1)
            b[i] = randint(-1, 1)            
            x += a[i] * speed
            y += b[i] * 2 * speed / 3
        else:
            x += a[i] * speed
            y += b[i] * 2 * speed / 3
    elif (x > 1100 or x < 100 or y < 100 or y > 700) and x != 0 and y != 0:
        if x < 100:
            a[i] = randint(0, 1)
            if 100 < y < 700:
                if a[i] == 0:
                     b[i] = choice([-1, 1])
                else:
                    b[i] = randint(-1, 1)
            elif y > 700:
                if a[i] == 0:
                    b[i] = -1
                else:
                    b[i] = randint(-1, 0)
            elif y < 100:
                if a[i] == 0:
                    b[i] = 1
                else:
                    b[i] = randint(0, 1)
        elif x > 1100:
            a[i] = randint(-1, 0)
            if y < 100:
                if a[i] == 0:
                    b[i] = 1
                else:
                    b[i] = randint(0, 1)
            if y > 700:
                if a[i] == 0:
                    b[i] = -1
                else:
                    b[i] = randint(-1, 0)
        elif 100 < x < 1100 and y < 100:
            a[i] = randint(-1, 1)
            if a[i] == 0:
                b[i] = 1
            else:
                b[i] = randint(0, 1)
        elif 100 < x < 1100 and y > 700:
            a[i] = randint(-1, 1)
            if a[i] == 0:
                b[i] = -1
            else:
                b[i] = randint(-1, 0)
        x += a[i] * speed
        y += b[i] * 2 * speed / 3
    else:
        x = randint(100, 1100)
        y = randint(100, 700)
        r = randint(25, 100)
        color = COLORS[randint(0, 5)]
        a[i] = randint(-1, 1)
        b[i] = randint(-1, 1)
        if a[i] == b[i] and a[i] == 0:
            a[i] = 1
    p[i][0] = x
    p[i][1] = y
    return p[i][0], p[i][1], p[i][2], p[i][3]

def click(event, c):
    '''
    checks the hit and counts the score
    c - list args [x, y, r]
    '''
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
        leaderboard(score)
        sort_file('leaderboard.txt')
        score = 0

def leaderboard(score):
    text = open('leaderboard.txt', 'r+')
    name = input('Your name is...')
    textfile = text.read()
    line = name, ' ', str(score), '\n'
    textfile = ''.join(line)
    text.write(textfile)
    text.close()

def sort_file(file):
    text = open(file, 'r+')
    textfile = text.readlines()
    names = []
    scores = []
    scores_names = []
    for el in textfile:
        names.append(el.split(' ')[0])
        scores.append(int(el.split(' ')[1]))
    for i in range(len(names)):
        elem = [scores[i], names[i]]
        scores_names.append(elem)
    scores_names.sort(reverse=True)
    text.seek(0)
    for line in range(len(textfile)):
        position = str(scores_names[line][1]) + ' ' + str(scores_names[line][0]) + '\n'
        text.write(position)
    text.close()
 

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
            for i in range(quantity):
                x = p[i][0]
                y = p[i][1]
                r = p[i][2]
                if (x - event.pos[0])**2 + (y - event.pos[1])**2 <= r**2:
                    p[i][0] = randint(100, 1100)
                    p[i][1] = randint(100, 700)
                    p[i][2] = randint(25, 100)
                    p[i][3] = COLORS[randint(0, 5)]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                None
            elif event.key == pygame.K_s:
                print('Score:', score)
    for i in range(quantity):   # create some balls with random args
        if len(p[i]) == 0:
            p[i] = list(xyr())      #   create start value of circle
            draw_ball(p[i])
        else:
            draw_ball(move(p[i]))   #   use chenged value of circle
    pygame.display.update()
    screen.fill(BLACK)
    

pygame.quit()
