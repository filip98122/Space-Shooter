import pygame
pygame.init()
WIDTH,HEIGHT=1540,900

class Power_up:
    def __init__(s,x,y,vrsta):
        s.x=x
        s.y=y
        s.speed=HEIGHT/306
        s.alive=True
        s.link=vrsta
        s.image=pygame.image.load(f"textures/powerup{vrsta}.png")
        s.height = HEIGHT/17
        s.width = HEIGHT/17
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def move_and_draw(s,window):
        s.y+=s.speed
        window.blit(s.scaled_img,(s.x,s.y))
        if s.y>=HEIGHT:
            s.alive=False