import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 800))
screen2 = pygame.display.set_mode((600,800))

# Colors
yellow = (255, 255, 0)
black = (0, 0, 0)
grey = (224, 224, 224)
red = (255, 0, 0)
olive = (128, 128, 0)
green =(0,255,0)
saddlebrown = (139, 69, 19)
white = (255, 255, 255)
aqua = (0, 255, 255)
coral=(255, 127, 80)
pi=3.14

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

def draw_cat(color,x,y,radius1,radius2):

    radius3=radius2/1.3
    radius4=radius2/1.3
    x2 = x - radius3/2

    y2 = y - radius4/4
    a=x2+radius3/4
    b= y2 + radius4 / 8
    c =x2+radius3/9
    d=y2+radius4/4.5
    a1=a+((radius3/100)*45)
    x3=x2+radius3
    c2=c+((radius3/100)*75)
    '''hvost'''
    ellipse(screen, coral, (x + radius1 * 0.7 + radius3 / 1.5, y + (radius2 * 0.3), radius1 * 0.7, radius2 * 0.3))
    ellipse(screen, black, (x + radius1 * 0.7 + radius3 / 1.5, y + (radius2 * 0.3), radius1 * 0.7, radius2 * 0.3), 1)

    '''правая нога'''
    ellipse(screen, coral, (x2 + (radius3 / 3)/2, y2 + radius4 / 1.5, radius3 / 3, radius4 / 1.5))
    ellipse(screen, black, (x2 + (radius3 / 3)/2, y2 + radius4 / 1.5, radius3 / 3, radius4 / 1.5), 1)
    '''тело и голова'''
    ellipse(screen, color, (x,y,radius1,radius2))
    ellipse(screen, black, (x, y, radius1, radius2),1)
    ellipse(screen, color, (x2,y2 , radius3, radius4))
    ellipse(screen, black, (x2, y2, radius3, radius4),1)
    '''левое ухо'''
    polygon(screen,black,[(a,b),(x2,y2),(a,b),(c,d),
                          (c,d),(x2,y2)] , 3)
    polygon(screen, coral, [(a, b), (x2, y2), (a, b), (c, d),
                            (c, d), (x2, y2)] )
    polygon(screen, black, [(a-((a/100)*6), b), (x2+((a/100)*10),y2+((a/100)*10)),
                          (a-((a/100)*6), b),(c,d-((a/100)*6)),
                          (c,d-((a/100)*6)),(x2+((a/100)*10),y2+((a/100)*10)) ], 2)
    polygon(screen, white, [(a - ((a / 100) * 6), b), (x2 + ((a / 100) * 10), y2 + ((a / 100) * 10)),
                            (a - ((a / 100) * 6), b), (c, d - ((a / 100) * 6)),
                            (c, d - ((a / 100) * 6)), (x2 + ((a / 100) * 10), y2 + ((a / 100) * 10))], )
    '''правое ухо'''

    polygon(screen,black,[(a1,b),(x3,y2),(a1,b),(c2,d),
                          (c2,d),(x3,y2)] , 3)
    polygon(screen, coral, [(a1, b), (x3, y2), (a1, b), (c2, d),
                            (c2, d), (x3, y2)], )
    polygon(screen, black, [((a1+((a/100)*6)), b), (x3-((a/100)*10),y2+((a/100)*10)),
                          (a1+((a/100)*6), b),(c2,d-((a/100)*6)),
                          (c2,d-((a/100)*6)),(x3-((a/100)*10),y2+((a/100)*10)) ], 2)
    polygon(screen, white, [((a1 + ((a / 100) * 6)), b), (x3 - ((a / 100) * 10), y2 + ((a / 100) * 10)),
                            (a1 + ((a / 100) * 6), b), (c2, d - ((a / 100) * 6)),
                            (c2, d - ((a / 100) * 6)), (x3 - ((a / 100) * 10), y2 + ((a / 100) * 10))], )
    '''рисуем глаза'''
    ellipse(screen, green, (x2+radius3/7,y2+radius4/5, radius3/4, radius4/3))
    ellipse(screen, black, (x2 + radius3 / 7, y2 + radius4 / 5, radius3 / 4, radius4 / 3),1)
    ellipse(screen, green, ((x2 + radius3 / 7)+radius3/2.1, y2 + radius4 / 5, radius3 / 4, radius4 / 3))
    ellipse(screen, black, ((x2 + radius3 / 7) + radius3 / 2.1, y2 + radius4 / 5, radius3 / 4, radius4 / 3),1)
    ellipse(screen, black, (x2 + radius3 / 4, y2 + radius4 / 5, radius3 / 16, radius4 / 3))
    ellipse(screen, black, ((x2 + radius3 / 4) + radius3 / 2.1, y2 + radius4 / 5, radius3 / 16, radius4 / 3))
    '''рисуем нос'''
    polygon(screen, black,[(x2+(radius3/2+radius3/12),y2+(radius3/2+radius3/12)),(x2+(radius3/2-radius3/12),y2+(radius3/2+radius3/12)),
                           (x2+(radius3/2-radius3/12),y2+(radius3/2+radius3/12)),(x2+radius3/2,y2+(radius3/2+radius3/12+radius3/12)),(x2+radius3/2,y2+(radius3/2+radius3/12+radius3/12)),(x2+(radius3/2+radius3/12),y2+(radius3/2+radius3/12))])
    '''рисуем рот'''
    line(screen, black,(x2+radius3/2,y2+(radius3/2+radius3/12+radius3/12)),(x2+radius3/2,y2+(radius3/2+radius3/12+radius3/12+radius3/12)),1)
    arc(screen, black,(x2+radius3/2,y2+(radius3/2+radius3/12+radius3/12),radius3/8,radius4/8),pi,2*pi,1)
    arc(screen, black, ((x2 + radius3 / 2)- radius3 / 9, y2 + (radius3 / 2 + radius3 / 12 + radius3 / 12), radius3 / 8, radius4 / 8),
        pi,  2*pi, 1)


    '''рисуем усы'''

    line(screen, black,(x2+(radius3/2+radius3/4),y2+(radius3/2+radius3/12+radius3/12)),(x2+(radius3/2+radius3/1.5),y2+(radius3/2+radius3/12+radius3/12)),1)

    line(screen, black, (x2 + (radius3 / 2 + radius3 / 4), y2 + (radius3 / 2 + radius3 / 12)),
         (x2 + (radius3 / 2 + radius3 / 1.5), y2 + (radius3 / 2 )), 1)
    line(screen, black, (x2 + (radius3 / 2 + radius3 / 4), y2 + (radius3 / 2 + radius3 / 12+ radius3 / 12+ radius3 / 12)),
         (x2 + (radius3 / 2 + radius3 / 1.5), y2 + (radius3 -radius3 / 8) ), 1)

    line(screen, black,
         (x2+radius3/4 , y2 + (radius3 / 2 + radius3 / 12 + radius3 / 12 + radius3 / 12)),
         (x2 - ( radius3 / 6), y2 + (radius3 - radius3 / 8)), 1)
    line(screen, black,
         (x2 + radius3 / 4, y2 + (radius3 / 2 + radius3 / 12 + radius3 / 12 )),
         (x2 - (radius3 / 6), y2 + (radius3/2 + radius3 / 12+ radius3 / 12 )), 1)
    line(screen, black,
         (x2 + radius3 / 4, y2 + (radius3 / 2 + radius3 / 12 )),
         (x2 - (radius3 / 6), y2 + (radius3/2 )), 1)
    '''рисуем лапы'''
    ellipse(screen, coral, (x2+radius3 / 2 , y2 + radius3*1.2, radius3 / 1.5, radius4 / 3))
    ellipse(screen, black, (x2+radius3 / 2 , y2 + radius3*1.2, radius3 / 1.5, radius4 / 3),1)
    '''рисуем заднюю лапу'''
    ellipse(screen, coral, (x+radius1*0.7, y+radius2*0.5 , radius3 * 0.9, radius4 * 0.9))
    ellipse(screen, black, (x+radius1*0.7, y+radius2*0.5 , radius3 * 0.9, radius4 * 0.9),1)
    ellipse(screen, coral, (x + radius1 * 0.7+radius3/1.5, y + (radius2 * 0.5)+(radius4/1.5), radius3 /3, radius4/1.5))
    ellipse(screen, black, (x + radius1 * 0.7+radius3/1.5, y + (radius2 * 0.5)+(radius4/1.5),  radius3 /3, radius4/1.5), 1)
    '''клубок'''
    circle(screen, grey,(x+radius2,y+radius1),radius3/3)
    circle(screen, black,(x+radius2,y+radius1),radius3/3,1)

draw_background(saddlebrown, 0, 0, 600, 300)
draw_background(olive, 0, 300, 600, 500)
draw_window(white, 390, 20, 200, 270,
            aqua)

draw_window(white, 110, 20, 200, 270,
            aqua)

draw_window(white, -160, 20, 200, 270,
            aqua)
draw_cat(coral, 200,320,300,150)
draw_cat(green, 100,220,150,75)
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
