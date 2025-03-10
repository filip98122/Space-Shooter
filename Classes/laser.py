import pygame
pygame.init()
import math
from Classes.player import *
WIDTH,HEIGHT=1540,900


class Laser:
    def __init__(s,x,health,angle,str=0,y=p1.y):
        s.x = x
        s.y=y
        s.angle=angle
        s.health = health
        s.scale = 0.3*0.75
        s.dy=-HEIGHT/109.2857142857143
        s.ddy=-HEIGHT/15300
        s.dx=0
        s.ddx=0
        s.img = pygame.image.load('textures/laser.png')
        s.width = s.img.get_width()*(HEIGHT/3400)
        s.height = s.img.get_height()*(HEIGHT/3400)
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        str+=1
        if s.angle==0:
            s.y-=s.height
        if p1.power_db>0:
            if str==2:
                if s.angle==0:
                    s.x-=s.width
                else:
                    s.y-=l_l[len(l_l)-1].width/2
            else:
                if s.angle!=0:
                    s.y+=l_l[len(l_l)-1].width/2
        else:
            s.x-=s.width/2
        if s.angle==45:
            s.dx=-HEIGHT/109.2857142857143
            s.ddx=-HEIGHT/15300
        elif s.angle==315:
            s.dx=HEIGHT/109.2857142857143
            s.ddx=HEIGHT/15300
        s.rotated_img=pygame.transform.rotate(s.scaled_img,s.angle)
    def draw(s,window):
        if s.health >0:
            if s.y <= -53*0.75:
                s.health =0
            s.y+=s.dy
            s.dy+=s.ddy
            s.x+=s.dx
            s.dx+=s.ddx
            window.blit(s.rotated_img,(s.x,s.y))
l_l = []