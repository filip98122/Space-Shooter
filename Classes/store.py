import pygame
pygame.init()
WIDTH,HEIGHT = 1540,900




class Store:
    def __init__(s,x,y,index,text,cost,quantity,op):
        s.x =x
        s.y=y
        s.quantity=quantity
        s.index=index
        s.op=op
        s.cost=cost
        s.img = pygame.image.load("textures/buttons.png")
        myfont = pygame.font.SysFont('B', int(WIDTH/17))
        s.text_surface = myfont.render(f"{text}", True, (255, 255, 255))
        s.width1=s.text_surface.get_width()
        s.height1=s.text_surface.get_height()
        s.width = s.width1+20
        s.height = s.height1+20
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
    def draw(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        window.blit(s.text_surface,(s.x+10,s.y+10))
