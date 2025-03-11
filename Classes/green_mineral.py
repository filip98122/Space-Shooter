import pygame
pygame.init()
WIDTH,HEIGHT=1540,900
class Green_Mineral:
    def __init__(s,x,y,dy):
        s.x = x
        s.y = y
        s.alive = True
        s.dy = dy
        s.img = pygame.image.load("textures/green mineral.png")
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.x-=s.width/2
    def move_and_draw(s,window):
        if s.alive == True:
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))