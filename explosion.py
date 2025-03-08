import pygame
pygame.init()
class Explosion:
    def __init__(s,x,y,w,h,time,ss):
        s.x= x
        s.y = y
        s.w = w
        s.h = h
        s.width1 = s.w
        s.height1 = s.h
        s.t = time
        s.Time_from_death = 0
        s.ss = ss
        
        s.images={}
        for i in range(7):
            s.img = pygame.image.load(f"explosion{i}.png")
            s.width1=s.w*s.ss
            s.height1=s.h*s.ss
            s.scaled_img1 = pygame.transform.scale(s.img, (s.width1, s.height1))
            s.images[i]=s.scaled_img1
    def draw(s,window):
        if s.t==0:
            window.blit(s.images[s.Time_from_death//5],(s.x,s.y))
        if s.t == 0:
            s.Time_from_death+=1
        else:
            s.t-=1