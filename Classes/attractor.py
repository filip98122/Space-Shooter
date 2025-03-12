import pygame
import random
pygame.init()
WIDTH,HEIGHT=1540,900
from Classes.loader import *
class Attractor:
    def __init__(s,x,y,prozor):
        s.x=x
        s.y=y
        s.prozor=prozor
        s.img = images['particle_red']
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.x+=s.width/2
        s.y+=s.height/2
    def draw(s,window):
        window.blit(s.scaled_img,(s.x-s.width/2,s.y-s.height/2))