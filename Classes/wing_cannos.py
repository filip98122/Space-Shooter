import pygame
pygame.init()
WIDTH,HEIGHT=1540,900
from Classes.loader import *
class Wing_cannons:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.img = images[28]
        s.width = s.img.get_width()*(HEIGHT/(3400*6))
        s.height = s.img.get_height()*(HEIGHT/(3400*6))
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.speed= HEIGHT/109
        s.ddy=-HEIGHT/15300
        s.alive=True
        s.x-=s.width/2
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.y-=s.speed
        s.speed-=s.ddy
        if s.y<0-s.height:
            s.alive=False