import pygame
pygame.init()
import math
from player import *
WIDTH,HEIGHT=1540,900
def Vector_Normalization(x1, y1, x2, y2):
    # Calculate dx and dy with direction
    distancex = x2 - x1
    distancey = y2 - y1
    vector_lenght=math.sqrt(distancex*distancex+distancey*distancey)
    distancex=distancex/vector_lenght
    distancey=distancey/vector_lenght
    distancex*=HEIGHT/150 # For speed
    distancey*=HEIGHT/150 # For speed
    return distancex,distancey
class Fireball:
    def __init__(s,x,y):
        s.health=1
        s.x=x
        s.y=y
        s.scale=HEIGHT/1800
        img1=pygame.image.load(f"fireball.png")
        s.width=img1.get_width()*s.scale
        s.height=img1.get_height()*s.scale
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.dx,s.dy=Vector_Normalization(s.x+s.width/2,s.y+s.height/2,p1.x+p1.width/2,p1.y+p1.height/2)
        s.x-=s.width/2
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.x+=s.dx
        s.y+=s.dy
        if s.x+s.width<=0 or s.x>=WIDTH or s.y>=HEIGHT or s.y+s.height<=0:
            s.health=0