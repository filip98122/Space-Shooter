import os
import pygame
import random
import math
import time
import json
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False


clock = pygame.time.Clock()
WIDTH,HEIGHT = 765,765
window = pygame.display.set_mode((WIDTH,HEIGHT))
def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

class Player:
    def __init__(s,x,y,dx,time,speed):
        s.x =x
        s.y=y
        s.dx=dx
        s.time=time
        s.speed = speed
        s.health = 3
        s.scale = 0.3*0.75
        if s.health ==3:
            s.img = pygame.image.load('full.png')
        if s.health==2:
            s.img = pygame.image.load('damaged1.png')
        if s.health==1:
            s.img = pygame.image.load('damaged2.png')
    def draw(self,window):
        
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
        window.blit(self.scaled_img,(self.x,self.y))
    def move(s,keys):
        s.dx = 0
        if s.x>=2:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                s.dx = -s.speed
        if s.x+s.width<763:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                s.dx = s.speed
        s.x+=s.dx
        if s.time>0:
            s.time-=1





class Laser:
    def __init__(self,x,health):
        self.x = x
        self.y = 510
        self.health = health
        self.dy = -7
        self.scale = 0.3*0.75
        self.img = pygame.image.load('laser.png')
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
    def draw(s,window):
        if s.health == 1:
            if s.y <= -53*0.75:
                s.health = 0
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))
        
l_l = []



p1 = Player(100,550,0,0,6)
        
        
while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_SPACE]:
        if p1.time == 0:
            p1.time = 20
            if len(l_l) == 40:
                for i in range(len(l_l)):
                    if l_l[i].health == 0:
                        if p1.health == 2 or p1.health == 3:
                            l_l[i] = Laser(p1.x+78*0.75,1)
                        else:
                            l_l[i] = Laser(p1.x+49*0.75,1)
            else:
                if p1.health == 2 or p1.health == 3:
                    l1 = Laser(p1.x+78*0.75,1)
                else:
                    l1 = Laser(p1.x+49*0.75,1)
                l_l.append(l1)
    for i in range(len(l_l)):
        if l_l[i].health != 0:
            l_l[i].draw(window)
    q = 0
    for i in range(len(l_l)):
        if l_l[q].health == 0:
            del l_l[q]
            q-=1
        q+=1
    p1.draw(window)
    p1.move(keys)
    pygame.display.update()
    clock.tick(60)