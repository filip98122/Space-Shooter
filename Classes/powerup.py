from Classes.loader import *
class Power_up:
    def __init__(s,x,y,vrsta):
        s.x=x
        s.y=y
        s.speed=HEIGHT/306
        s.alive=True
        s.link=vrsta
        if s.link=="db":
            s.image=images[26]
        else:
            s.image=images[27]
        s.height = HEIGHT/17
        s.width = HEIGHT/17
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def move_and_draw(s,window):
        s.y+=s.speed
        window.blit(s.scaled_img,(s.x,s.y))
        if s.y>=HEIGHT:
            s.alive=False