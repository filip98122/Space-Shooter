from Classes.loader import *
class Drone:
    def __init__(s,x,y,str):
        s.x=x
        s.y=y
        s.img = images[29]
        s.width = HEIGHT/18
        s.height = HEIGHT/18
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.speed= WIDTH/90
        s.x-=s.width/2
        s.speed*=str
        s.str=str
        s.health=10
        s.shoot=random.randint(240,300)
        s.xo=s.x
        s.stop=1
        s.dx=(WIDTH/4)/90
        s.dx*=s.str
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.shoot-=1
        if s.str==1:
            if s.x<s.xo+WIDTH and s.stop==1:
                s.x+=s.speed
            else:
                if s.stop==1:
                    s.stop=0
                    s.x=s.xo+WIDTH
                if s.stop ==0:
                    if s.x>=s.xo+WIDTH+WIDTH/4 or s.x<=s.xo+WIDTH/4:
                        s.dx*=-1
                    s.x+=s.dx
        else:
            if s.x>s.xo-WIDTH and s.stop==1:
                    s.x+=s.speed
            else:
                if s.stop==1:
                    s.stop=0
                    s.x=s.xo-WIDTH
                if s.stop==0:
                    if s.x>=s.xo-WIDTH+WIDTH/4:
                        s.dx*=-1
                    if s.x<=s.xo-WIDTH-WIDTH/4:
                        s.dx*=-1
                    s.x+=s.dx