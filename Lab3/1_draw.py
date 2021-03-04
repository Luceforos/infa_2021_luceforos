import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
yellow=(255,255,0)
black= (0,0,0)
grey=(224,224,224)
red=(255,0,0)
def draw_backscreen(color):
    rect(screen, color, (0, 0, 400, 400))

def draw_smileface(color1,color2, x,y,radius,outline):
    circle(screen, color1, (x, y), radius)#main
    circle(screen, color2, (x, y), radius, outline)#outline

def draw_eyebrows(color,x1,y1,x2,y2,weight):
    line(screen, color, (x1,y1), (x2,y2),weight)

def draw_eyes(color1,color2,color3,
             x1,y1,x2,y2,x3,y3,
             radius1,radius2,radius3,
             outline):

    circle(screen,color1,(x1,y1),radius1)
    circle(screen,color2,(x2,y2),radius2,outline)
    circle(screen, color3, (x3, y3), radius3)

def draw_mouth(color,x1,y1,x2,y2,weight):
    line(screen, color, (x1,y1), (x2,y2),weight)
draw_backscreen(grey)
draw_smileface(yellow,black, 200,200,100,2)
draw_eyebrows(black,170,170,90,130,10)#left
draw_eyebrows(black, 220,170, 290,140,10)#right
draw_eyes(red,black,black,          #left
          150,200,150,200,150,200,
          30,30,10,
          3)
draw_eyes(red,black,black,          #right
          250,200,250,200,250,200,
          20,20,5,
          3)

draw_mouth(black,150,260,250,260,10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()