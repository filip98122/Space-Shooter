import pygame
pygame.init()
import math
from Classes.fireball import *
WIDTH,HEIGHT=1540,900
class Boss:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.scale=HEIGHT/900
        img1=pygame.image.load(f"textures/boss.png")
        s.width=img1.get_width()*s.scale
        s.height=img1.get_height()*s.scale
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.shoot=0
        s.x-=s.width/2
        s.health = 75
    def general(s,window,l_f):
        window.blit(s.scaled_img,(s.x,s.y))
        if s.shoot==0:
            s.make_fireball(l_f)
            s.shoot=50
        else:
            s.shoot-=1
    def make_fireball(s,l_f):
        l_f.append(Fireball(s.x+s.width/2,s.y+s.height))
boss = Boss(WIDTH/2,100)