import pygame
from pygame.draw import *

pygame.init()
def draw_backscreen(color):
    rect(screen, color, (0, 0, 400, 400))

def draw_smileface(color1,color2, x,y,radius,outline):
    circle(screen, color1, (x, y), radius)#main
    circle(screen, color2, (x, y), radius, outline)#outline

def draw_eyebrows(color,x1,y1,x2,y2,weight):
    line(screen, color, (x1,y1), (x2,y2),weight)

FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow=(255,255,0)
N = 10
black= (0,0,0)
grey=(224,224,224)
red=(255,0,0)
draw_backscreen(grey)
draw_smileface(yellow,black, 200,200,100,2)
draw_eyebrows(black,170,170,90,130,10)#left
draw_eyebrows(black, 220,170, 290,140,10)#right
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