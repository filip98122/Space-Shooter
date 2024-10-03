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
        s.scale = 0.3
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
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            s.dx = -s.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            s.dx = s.speed
        s.x+=s.dx
p1 = Player(100,550,0,0,4)
        
        
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
    p1.move(keys)
    p1.draw(window)
    pygame.display.update()
    clock.tick(60)