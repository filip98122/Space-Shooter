from Classes.loader import *
class Boss_healthmeter:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.scale=HEIGHT/(900*4)
        img1=images[31]
        s.width=HEIGHT/3
        s.height=HEIGHT/18
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.x-=s.width/2
        s.offsetx=s.width/8
        s.offsety=s.height/3.333333333333333
    def draw(s,window,bosshealth):
        for i in range(bosshealth):
            pygame.draw.rect(window,("red"),pygame.Rect(s.x+(i*((s.width-(s.offsetx*2))/75))+s.offsetx,s.y+s.offsety,(s.width-(s.offsetx*2))/75,s.height-(s.offsety*2)))
        window.blit(s.scaled_img,(s.x,s.y))