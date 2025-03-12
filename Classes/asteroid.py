import pygame
import random
pygame.init()
WIDTH,HEIGHT=1540,900
from Classes.loader import *
class Asteroid:
    def __init__(s,x,y,alive):
        s.x = x
        s.y = y
        s.drop=True
        s.strana=random.randint(0,1)
        s.alive =alive
        s.Time_from_death = 70
        s.img_choice = random.randint(1,4)
        s.speed = random.randint(int(HEIGHT/382.5),int(HEIGHT/153))
        if s.img_choice == 1:
            s.image = images['asteroid1']
        if s.img_choice == 2:
            s.image = images['asteroid2']
        if s.img_choice == 3:
            s.image = images['asteroid3']
        if s.img_choice == 4:
            s.image = images['asteroid4']
            
        
        s.height = int(HEIGHT/16.6304347826087)
        s.width = int(HEIGHT/16.6304347826087)
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def draw(s,window):
        if s.alive >= 0:
            window.blit(s.scaled_img,(s.x,s.y))
            s.y+=s.speed