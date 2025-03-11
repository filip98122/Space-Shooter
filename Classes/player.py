import pygame
pygame.init()
WIDTH,HEIGHT=1540,900
class Player:
    """Moves and draws the player"""
    def __init__(s,x,y,dx,time,speed):
        s.x =x
        s.y=y
        s.dx=dx
        s.time=time
        s.speed = speed
        s.health = 3
        s.scale = HEIGHT/3400
        s.power_rb=0
        s.power_db=0
        s.time_missle=0
        s.dy=0
        scale=HEIGHT/5940.594059405941
        img = pygame.image.load('textures/1c.png')
        s.height = img.get_height()*scale
        s.width = s.height
        e=pygame.transform.scale(img, (s.width, s.height))
        
        
        img = pygame.image.load('textures/2.png')
        s.height = img.get_height()*scale
        s.width = s.height
        w=pygame.transform.scale(img, (s.width, s.height))
        
        
        
        img = pygame.image.load('textures/3.png')
        s.height = img.get_height()*scale
        s.width=s.height
        q=pygame.transform.scale(img, (s.width, s.height))
        
        
        
        s.y-=s.height*(HEIGHT/600)
        s.x-=s.width/2
        
        
        img = pygame.image.load('textures/1l.png')
        s.height = img.get_height()*scale
        s.width=s.height
        t=pygame.transform.scale(img, (s.width, s.height))
        
        img = pygame.image.load('textures/1r.png')
        s.height = img.get_height()*scale
        s.width=s.height
        r=pygame.transform.scale(img, (s.width, s.height))
        s.str=""
        
        
        s.dict={
            3:q,
            2:w,
            "1c":e,
            "1l":t,
            "1r":r
            
        }
        

        

        
    def draw(s,window):
        if s.health<=0:
            return
        else:
            if s.health!=1:
                s.width=s.dict[s.health].get_width()
                s.height=s.dict[s.health].get_height()
                window.blit(s.dict[s.health],(s.x,s.y))
            else:
                s.width=s.dict[f'{s.health}{s.str}'].get_width()
                s.height=s.dict[f'{s.health}{s.str}'].get_height()
                window.blit(s.dict[f'{s.health}{s.str}'],(s.x,s.y))
    def move(s,keys):
        s.dx = 0
        s.dy=0
        if s.x>=0:
            if keys["left"]:
                s.dx -= s.speed
        if s.x+s.width<WIDTH:
            if keys["right"]:
                s.dx += s.speed
        if s.y<HEIGHT-s.height:
            if keys["down"]:
                s.dy+=s.speed
        if s.y>0:
            if keys["up"]:
                s.dy-=s.speed
        s.y+=s.dy
        s.x+=s.dx
        if s.time>0:
            s.time-=1
        if s.time_missle>0:
            s.time_missle-=1
        if s.power_rb>0:
            s.power_rb-=1
        if s.power_db>0:
            s.power_db-=1
p1 = Player(WIDTH/2,HEIGHT,0,0,WIDTH/160)