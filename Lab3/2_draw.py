import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 800))
# Colors
yellow = (255, 255, 0)
black = (0, 0, 0)
grey = (224, 224, 224)
red = (255, 0, 0)
olive = (128, 128, 0)
saddlebrown = (139, 69, 19)
white = (255, 255, 255)
aqua = (0, 255, 255)


def draw_background(color, x1, y1, x2, y2):
    rect(screen, color, (x1, y1, x2, y2))


def draw_window(color1, x1, y1, x2, y2,
                color2):
    ''' Расчет размера и положения стекол, относительно размера окна '''
    x3 = x1 + x1 / 100 * 2
    y3 = y1 + y1 / 100 * 10
    x4 = x2 / 100 * 40
    y4 = y2 / 100 * 25
    x5 = x1 + x2 - x4 - x1 / 100 * 2
    y5 = y1 + x4 + x4 / 100 * 10
    '''Рисуем окно и стекла'''
    rect(screen, color1, (x1, y1, x2, y2))
    rect(screen, color2, (x3, y3, x4, y4))
    rect(screen, color2, (x5, y3, x4, y4))
    rect(screen, color2, (x3, y5, x4, y4 * 2.5))
    rect(screen, color2, (x5, y5, x4, y4 * 2.5))


def draw_smileface(color1, color2, x, y, radius, outline):
    circle(screen, color1, (x, y), radius)  # main
    circle(screen, color2, (x, y), radius, outline)  # outline


def draw_eyebrows(color, x1, y1, x2, y2, weight):
    line(screen, color, (x1, y1), (x2, y2), weight)


def draw_eyes(color1, x1, y1, radius1,
              color2, x2, y2, radius2, outline,
              color3, x3, y3, radius3,
              ):
    circle(screen, color1, (x1, y1), radius1)
    circle(screen, color2, (x2, y2), radius2, outline)
    circle(screen, color3, (x3, y3), radius3)


def draw_mouth(color, x1, y1, x2, y2, weight):
    line(screen, color, (x1, y1), (x2, y2), weight)


draw_background(saddlebrown, 0, 0, 600, 300)
draw_background(olive, 0, 300, 600, 500)
draw_window(white, 390, 20, 200, 270,
            aqua)

'''draw_smileface(yellow, black, 200, 200, 100, 2)
draw_eyebrows(black, 170, 170, 90, 130, 10)  # left
draw_eyebrows(black, 220, 170, 290, 140, 10)  # right
draw_eyes(red, 150, 200, 30,  # left
          black, 150, 200, 30, 3,
          black, 150, 200, 10,
          )
draw_eyes(red, 250, 200, 20,  # right
          black, 250, 200, 20, 3,
          black, 250, 200, 5,
          )

draw_mouth(black, 150, 260, 250, 260, 10)'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
