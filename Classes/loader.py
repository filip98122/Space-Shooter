import pygame
import random
from cryptography.fernet import Fernet
pygame.init()
WIDTH,HEIGHT=1540,900
class Loader():
    def load(s):
        loaded={}
        s.image1 = pygame.image.load("textures/asteroid1.png")
        s.image2= pygame.image.load("textures/asteroid2.png")
        s.image3 = pygame.image.load("textures/asteroid3.png")
        s.image4 = pygame.image.load("textures/asteroid4.png")
        s.image5 = pygame.image.load("textures/particle_red.png")
        
        
        loaded[6]= pygame.image.load('textures/star1.png')
        loaded[7]=pygame.image.load('textures/star3.png')
        loaded[8]=pygame.image.load('textures/star2.png')
        loaded[9]=pygame.image.load(f"textures/boss.png")
        for i in range(10,17):
            loaded[i] = pygame.image.load(f"textures/explosion{i-10}.png")
        loaded[17]=pygame.image.load(f"textures/fireball.png")
        loaded[18]=pygame.image.load("textures/green mineral.png")
        loaded[19]=pygame.image.load('textures/laser.png')
        loaded[20]=pygame.image.load("textures/mineral.png")
        loaded[21]=pygame.image.load('textures/1c.png')
        loaded[22]=pygame.image.load('textures/2.png')
        loaded[23]=pygame.image.load('textures/3.png')
        loaded[24]=pygame.image.load('textures/1l.png')
        loaded[25]=pygame.image.load('textures/1r.png')
        loaded[26]=pygame.image.load('textures/powerupdb.png')
        loaded[27]=pygame.image.load('textures/poweruprb.png')
        loaded[28]=pygame.image.load("textures/bullet.png")
        
        loaded['asteroid1']=s.image1
        loaded['asteroid2']=s.image2
        loaded['asteroid3']=s.image3
        loaded['asteroid4']=s.image4
        loaded['particle_red']=s.image5
        return loaded
loader=Loader()
images=loader.load()