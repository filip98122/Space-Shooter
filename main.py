import os
import pygame
import random
import math
import time
import json
pygame.init()
pygame.mixer.init()
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False


clock = pygame.time.Clock()
WIDTH,HEIGHT = 765,765
window = pygame.display.set_mode((WIDTH,HEIGHT))
def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

class Background:
    def __init__(s,x,speedy):
        s.x = x
        s.y = 0
        s.scale = 9
        s.speedy = speedy
        s.d = random.randint(1,5)
        if s.d == 1:
            s.image = pygame.image.load('star1.png')
            s.width = s.image.get_width()/2.1
            s.height = s.image.get_height()/2.1
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d >= 3:
            s.image = pygame.image.load('star3.png')
            s.width = s.image.get_width()
            s.height = s.image.get_height()
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d == 2:
            s.image = pygame.image.load('star2.png')
            s.width = s.image.get_width()/1.8
            s.height = s.image.get_height()/1.8
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def move_and_draw(s,window):
        s.y+=s.speedy
        window.blit(s.scaled_img,(s.x,s.y))
l_b = []
class Player:
    def __init__(s,x,y,dx,time,speed):
        s.x =x
        s.y=y
        s.dx=dx
        s.time=time
        s.cant_go_left = False
        s.cant_go_right = False
        s.speed = speed
        s.health = 3
        s.scale = 0.3*0.75
        if s.health ==3:
            s.img = pygame.image.load('full.png')
        if s.health==2:
            s.img = pygame.image.load('damaged1.png')
        if s.health==1:
            s.img = pygame.image.load('damaged2.png')
    def draw(self,window):
        
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
        window.blit(self.scaled_img,(self.x,self.y))
    def move(s,keys):
        s.dx = 0
        s.cant_go_left = False
        s.cant_go_right = False
        if s.x>=2:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if keys[pygame.K_d] == False or keys[pygame.K_RIGHT] == False:
                    s.dx = -s.speed
        else:
            s.cant_go_left = True
        if s.x+s.width<763:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if s.dx == 0:
                    s.dx = s.speed
        else:
            s.cant_go_right = True
        s.x+=s.dx
        if s.time>0:
            s.time-=1


class Minerl:
    def __init__(s,x,y,dy):
        s.x = x
        s.y = y
        s.alive = True
        s.dy = dy
        s.img = pygame.image.load("mineral.png")
        s.width = 30
        s.height = 30
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
    def move_and_draw(s,window):
        if s.alive == True:
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))
            if s.y >= 770:
                s.alive = False
l_m = []
class Asteroid:
    def __init__(s,x,y):
        s.x = x
        s.y = y
        s.alive = True
        s.Time_from_death = 70
        s.img_choice = random.randint(1,4)
        s.speed = random.randint(2,5)
        if s.img_choice == 1:
            s.image = pygame.image.load("asteroid1.png")
        if s.img_choice == 2:
            s.image = pygame.image.load("asteroid2.png")
        if s.img_choice == 3:
            s.image = pygame.image.load("asteroid3.png")
        if s.img_choice == 4:
            s.image = pygame.image.load("asteroid4.png")
            
        
        s.height = s.image.get_height()*2
        s.width = s.image.get_width()*2
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def draw(s,window):
        if s.alive == True:
            window.blit(s.scaled_img,(s.x,s.y))
            s.y+=s.speed






l_a = []
l_e = []
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
    def draw(s,window):
        s.width1 = s.h
        s.height1 = s.h
        # Filip big-brain implementation
        s.img = pygame.image.load(f"explosion{s.Time_from_death//5}.png")
        s.width1*=s.ss
        s.height1*=s.ss
        s.scaled_img1 = pygame.transform.scale(s.img, (s.width1, s.height1))
        if s.t==0:
            window.blit(s.scaled_img1,(s.x,s.y))
        if s.t == 0:
            s.Time_from_death+=1
        else:
            s.t-=1
    
class Laser:
    def __init__(self,x,health):
        self.x = x
        self.y = 510
        self.health = health
        self.dy = -7
        self.scale = 0.3*0.75
        self.img = pygame.image.load('laser.png')
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
    def draw(s,window):
        if s.health == 1:
            if s.y <= -53*0.75:
                s.health = 0
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))
        
l_l = []



p1 = Player(100,550,0,0,6)

def draw_minerals(x,y,window,minerala):
    img = pygame.image.load("mineral.png")
    width = 30
    height = 30
    scaled_img = pygame.transform.scale(img, (width, height))
    window.blit(scaled_img,(x,y))
    myfont = pygame.font.SysFont('B', 45)
    text_surface = myfont.render(f"{minerala}", True, (255, 255, 255))
    window.blit(text_surface,(x+55,y))

minerala_ukupno = 0
minerala = 0
while True:
    a_r = random.randint(1,10)
    if a_r == 1:
        ast = Asteroid(random.randint(25,700),-70)
        l_a.append(ast)
    e = random.randint(1,20)
    if e == 1:
        w = random.randint(2,5)
        e = random.randint(10,728)
        l_b.append(Background(e,w))
    window.fill("Black")
    for i in range(len(l_b)):
        l_b[i].move_and_draw(window)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
    if p1.health==0:
        exit()
    draw_minerals(25,25,window,minerala)   
    
    
        
    #laser
    q = 0
    for i in range(len(l_l)):
        if l_l[q].health == 0:
            del l_l[q]
            q-=1
        q+=1
    r = 0
    
    if keys[pygame.K_SPACE]:
        if p1.time == 0:
            p1.time = 20
            if len(l_l) == 40:
                for i in range(len(l_l)):
                    if l_l[i].health == 0:
                        if p1.health == 2 or p1.health == 3:
                            l_l[i] = Laser(p1.x+78*0.75,1)
                        else:
                            l_l[i] = Laser(p1.x+49*0.75,1)
            else:
                if p1.health == 2 or p1.health == 3:
                    l1 = Laser(p1.x+78*0.75,1)
                else:
                    l1 = Laser(p1.x+49*0.75,1)
                l_l.append(l1)
    for i in range(len(l_l)):
        if l_l[i].health != 0:
            l_l[i].draw(window)

    
    #background
    if keys[pygame.K_h]:
        if minerala>=35:
            if p1.health!=3:
                p1.health+=1
                if p1.health==2:
                    p1.img = pygame.image.load('damaged1.png')
                if p1.health==3:
                    p1.img = pygame.image.load('full.png')
    for i in range(len(l_b)):
        if l_b[r].y >= 765:
            del l_b[r]
            r-=1
        r+=1
    
    #asteroids
    for i in range(len(l_a)):
        l_a[i].draw(window)
    r = 0
    for i in range(len(l_a)):
        if l_a[r].y >= 765:
            del l_a[r]
            r-=1
        r+=1
        
    err = 0
    for i in range(len(l_a)):
        if colision1(pygame.Rect(p1.x,p1.y,p1.width,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
            p1.health-=1
            if p1.health==2:
                p1.img = pygame.image.load('damaged1.png')
            if p1.health==1:
                p1.img = pygame.image.load('damaged2.png')
            del l_a[err]
            err-=1
        err +=1
    for i in range(len(l_l)):
        for j in range(len(l_a)):
            if colision1(pygame.Rect(l_l[i].x,l_l[i].y,l_l[i].width,l_l[i].height),pygame.Rect(l_a[j].x,l_a[j].y,l_a[j].width,l_a[j].height)):
                if l_a[j].alive == True:
                    l_l[i].health-=1
                    l_a[j].alive = False
    err = 0
    for i in range(len(l_a)):   
        if l_a[err].alive == False:
            m = Minerl(l_a[err].x,l_a[err].y,2.5)
            l_m.append(m)
            for i in range(5):
                timeSpread = i*5
                scalespread = 1.8-(i/10)*2
                e = Explosion(random.randint(l_a[err].x-30,l_a[err].x+l_a[err].width-10),random.randint(l_a[err].y-30,l_a[err].y+l_a[err].height-10),l_a[err].width,l_a[err].height,timeSpread,scalespread)
                l_e.append(e)
            del l_a[err]
            err-=1
        err+=1
    
    err = 0
    for i in range(len(l_e)):
        l_e[i].draw(window)
    for i in range(len(l_e)):
        if l_e[err].Time_from_death == 35:
            del l_e[err]
            err-=1
        err+=1
    for i in range(len(l_m)):
        l_m[i].move_and_draw(window)
    err = 0
    for i in range(len(l_m)):
        if l_m[err].alive == False:
            del l_m[err]
            err-=1
        err+=1
    for i in range(len(l_m)):
        if colision1(pygame.Rect(l_m[i].x,l_m[i].y,l_m[i].width,l_m[i].height),pygame.Rect(p1.x,p1.y,p1.width,p1.height)):
            minerala +=1
            minerala_ukupno +=1
            l_m[i].alive = False
            
    err = 0
    for i in range(len(l_m)):
        if l_m[err].alive == False:
            del l_m[err]
            err-=1
        err+=1
        
    p1.draw(window)
    p1.move(keys)
    pygame.display.update()
    clock.tick(60)