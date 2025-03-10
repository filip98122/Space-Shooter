import pygame
pygame.init()
class Button:
    def __init__(s,x,y,img,text,font,prozor,scale,scale1):
        s.x=x
        s.y=y
        s.scale=2.8
        s.scale=scale
        s.scale1=scale1
        s.prozor = prozor
        s.text=text
        img1=pygame.image.load(f"textures/{img}.png")
        s.width=img1.get_width()*s.scale
        s.height=img1.get_height()*s.scale1
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.x-=s.width/2
        s.y-=s.height/2
        if text!="":
            s.text_surface = font.render(f"{text}", True, (15, 15, 15))
            s.width1=s.text_surface.get_width()
            s.height1=s.text_surface.get_height()
            s.x1=s.x+((s.width-s.width1)//2)
            s.y1=s.y+((s.height-s.height1)//2)
    def draw(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        if s.text!="":
            window.blit(s.text_surface,(s.x1,s.y1))