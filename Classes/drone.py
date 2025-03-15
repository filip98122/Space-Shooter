import pygame
pygame.init()
WIDTH,HEIGHT=1540,900
from Classes.loader import *
class Drone:
    def __init__(s,x,y,str):
        s.x=x
        s.y=y
        s.img = images[29]
        s.width = HEIGHT/18
        s.height = HEIGHT/18
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.speed= WIDTH/90
        s.speed*=str
        s.str=str
        s.health=10
        s.xo=s.x
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        if s.str==1:
            if s.x<s.xo+WIDTH:
                s.x+=s.speed
        else:
            if s.x>s.xo-WIDTH:
                s.x+=s.speed
            else:
                s.x=s.xo-WIDTH