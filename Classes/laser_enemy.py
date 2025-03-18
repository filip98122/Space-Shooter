
from Classes.loader import *
class Laser_enemy:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.img = images[30]
        s.width = 64*(HEIGHT/3400)
        s.height = 176*(HEIGHT/3400)
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.dy=HEIGHT/220
        s.ddy=HEIGHT/15300
        s.alive=True
        s.x-=s.width/2
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.y+=s.dy
        s.dy+=s.ddy
        if s.y>HEIGHT:
            s.alive=False