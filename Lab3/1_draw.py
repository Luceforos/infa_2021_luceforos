import pygame
from pygame.draw import *

pygame.init()
def draw_backscreen(color):
    rect(screen, color, (0, 0, 400, 400))

def draw_smileface(color x,y):
FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow=(255,255,0)
N = 10
black= (0,0,0)
grey=(224,224,224)
red=(255,0,0)
draw_backscreen(grey)

#draw smileface
circle(screen,yellow,(200,200),100,0)
circle(screen,black,(200,200),100,2)
#draw left eyebrows
line(screen, black, (170,170), (90,130),10)
#draw right eyebrows
line(screen, black, (220,170), (290,140),10)
#draw left eye
circle(screen,red,(150,200),30,)
circle(screen,black,(150,200),30,3)
circle(screen,black,(150,200),10)
#draw left eye
circle(screen,red,(250,200),20,)
circle(screen,black,(250,200),20,3)
circle(screen,black,(250,200),5)
#draw mouth
line(screen, black, (150,260), (250,260),10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()