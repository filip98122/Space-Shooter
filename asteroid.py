import pygame
import random
pygame.init()
WIDTH,HEIGHT=1540,900
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
            s.image = pygame.image.load("asteroid1.png")
        if s.img_choice == 2:
            s.image = pygame.image.load("asteroid2.png")
        if s.img_choice == 3:
            s.image = pygame.image.load("asteroid3.png")
        if s.img_choice == 4:
            s.image = pygame.image.load("asteroid4.png")
            
        
        s.height = int(HEIGHT/16.6304347826087)
        s.width = int(HEIGHT/16.6304347826087)
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def draw(s,window):
        if s.alive >= 0:
            window.blit(s.scaled_img,(s.x,s.y))
            s.y+=s.speed