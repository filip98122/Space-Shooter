import os
import pygame
import random
import math
import time
import json
pygame.init()
pygame.mixer.init()
keys = pygame.key.get_pressed()
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

char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def checker(keys,index):
    pressed = 0
    for key in range(512):
        if keys[key]:
            pressed = key
            break
    if pressed!=0 and pressed!=kojih and pressed!=kojis and pressed!=kojid and pressed!=kojil:
        return pressed
    else:
        return index

keydict={
    "shot":keys[pygame.K_SPACE],
    "left":keys[pygame.K_a],
    "right":keys[pygame.K_d],
    "heal":keys[pygame.K_h]
    
}
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
        s.scale = 0.225
        
        
        
        
        s.img = pygame.image.load('1.png')
        s.width = s.img.get_width()*s.scale
        s.height = s.img.get_height()*s.scale
        e=pygame.transform.scale(s.img, (s.width, s.height))
        
        
        s.img = pygame.image.load('2.png')
        s.width = s.img.get_width()*s.scale
        s.height = s.img.get_height()*s.scale
        w=pygame.transform.scale(s.img, (s.width, s.height))
        
        
        
        s.img = pygame.image.load('3.png')
        s.width = s.img.get_width()*s.scale
        s.height = s.img.get_height()*s.scale
        q=pygame.transform.scale(s.img, (s.width, s.height))
        
        s.dict={
            3:q,
            2:w,
            1:e 
        }
        

        
    def draw(self,window):
        if self.health==0:
            return
        else:
            self.width=self.dict[self.health].get_width()
            self.height=self.dict[self.health].get_height()
            window.blit(self.dict[self.health],(self.x,self.y))
    def move(s,keys):
        s.dx = 0
        s.cant_go_left = False
        s.cant_go_right = False
        if s.x>=2:
            if keys["left"]:
                if keys["right"] == False:
                    s.dx = -s.speed
        else:
            s.cant_go_left = True
        if s.x+s.width<763:
            if keys["right"]:
                if s.dx == 0:
                    s.dx = s.speed
        else:
            s.cant_go_right = True
        s.x+=s.dx
        if s.time>0:
            s.time-=1


class Mineral:
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
        s.drop=True
        s.strana=random.randint(0,1)
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
        self.ddy=-0.05
        self.img = pygame.image.load('laser.png')
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
    def draw(s,window):
        if s.health == 1:
            if s.y <= -53*0.75:
                s.health = 0
            s.y+=s.dy
            s.dy+=s.ddy
            window.blit(s.scaled_img,(s.x,s.y))

class Button:
    def __init__(self,x,y,img,text,font,prozor,scale):
        self.x=x
        self.y=y
        if scale==None:
            self.scale=2.8
        else:
            self.scale=scale
        self.prozor = prozor
        self.text=text
        img1=pygame.image.load(f"{img}.png")
        self.width=img1.get_width()*self.scale
        self.height=img1.get_height()*self.scale
        self.scaled_img=pygame.transform.scale(img1,(self.width,self.height))
        if text!="":
            self.text_surface = font.render(f"{text}", True, (15, 15, 15))
            self.width1=self.text_surface.get_width()
            self.height1=self.text_surface.get_height()
    def draw(self,window):
        window.blit(self.scaled_img,(self.x,self.y))
        if self.text!="":
            window.blit(self.text_surface,(self.x+((self.width-self.width1)//2),self.y+((self.height-self.height1)//2)))
l_l = []
start=50
def mainmenu():
    global ukupnom
    global minerala
    l_a=[]
    l_l=[]
    l_e=[]
    l_m=[]
    p1.health=3
    ukupnom+=minerala
    minerala=0
    prozor=0
    return l_a,l_l,prozor,l_e,l_m

def change(index1,index2,index1c,index2c):
    info[index1]+=index1c
    info[index2]+=index2c
def read():
    f=open("infojson.json","r")
    info=f.read()
    info =json.loads(info)
    f.close()
    return info

info=read()

def write(info):
    f=open("infojson.json","w")
    info["minerala"]=ukupnom
    info=json.dumps(info)
    f.write(info)
    f.close()



myfont1 = pygame.font.SysFont('s', 60)

p1 = Player(100,550,0,0,9)

myfont = pygame.font.SysFont('s', 70)

lb=[Button(228.5,200,"start","",0,0,None),
    Button(228.5,400,"settings","",0,0,None),
    Button(228.5,600,"shop","",0,0,None),
    Button(60,start-25,"zapucanje","Change shoot key from Space",myfont1,2,6),
    Button(60,start+150,"zapucanje","Change go left key from a",myfont1,2,6),
    Button(60,start+325,"zapucanje","Change go right key from d",myfont1,2,6),
    Button(60,start+500,"zapucanje","Change heal key from h",myfont1,2,6)
    
]
def draw_minerals(x,y,window,minerala):
    img = pygame.image.load("mineral.png")
    width = 30
    height = 30
    scaled_img = pygame.transform.scale(img, (width, height))
    window.blit(scaled_img,(x,y))
    myfont = pygame.font.SysFont('B', 45)
    text_surface = myfont.render(f"{minerala}", True, (255, 255, 255))
    window.blit(text_surface,(x+55,y))
kojis=pygame.K_SPACE
kojil=pygame.K_a
kojid=pygame.K_d
kojih=pygame.K_h
ukupnom=info["minerala"]
minerala = 0
prozor=0
washolding=False
while True:
    if prozor==3:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                prozor=0
        if keys[pygame.K_ESCAPE]:
            prozor=0
            washolding=True
        e = random.randint(1,10)
        if e == 1:
            w = random.randint(2,5)
            e = random.randint(10,728)
            l_b.append(Background(e,w))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==3:
                lb[i].draw(window)
    if prozor==2:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                prozor=0
        if keys[pygame.K_ESCAPE]:
            prozor=0
            washolding=True
        e = random.randint(1,10)
        if e == 1:
            w = random.randint(2,5)
            e = random.randint(10,728)
            l_b.append(Background(e,w))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==2:
                lb[i].draw(window)
        #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
        #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
        #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[3].width,lb[3].height,lb[3].x,lb[3].y,mousePos,mouseState):
            q = checker(keys,kojis)
            if q==32:
                lb[3].text_surface = myfont1.render(f"Change shoot key from Space", True, (15, 15, 15))
            if q>=33 and q<=126:
                kojis=q
                lb[3].text_surface = myfont1.render(f"Change shoot key from {char[kojis-34]}", True, (15, 15, 15))

    #GOING LEFT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[4].width,lb[4].height,lb[4].x,lb[4].y,mousePos,mouseState):
            q = checker(keys,kojil)
            if q==32:
                lb[4].text_surface = myfont1.render(f"Change go left key from Space", True, (15, 15, 15))
            if q>=33 and q<=126:
                kojil=q
                lb[4].text_surface = myfont1.render(f"Change go left key from {char[kojil-34]}", True, (15, 15, 15))

    #GOING RIGHT CODE BELOW |||||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW |||||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW |||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[5].width,lb[5].height,lb[5].x,lb[5].y,mousePos,mouseState):
            q = checker(keys,kojid)
            if q==32:
                lb[5].text_surface = myfont1.render(f"Change sgo right key from Space", True, (15, 15, 15))
            if q>=33 and q<=126:
                kojid=q
                lb[5].text_surface = myfont1.render(f"Change go right key from {char[kojid-34]}", True, (15, 15, 15))

    #HEALING CODE BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW |||||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[6].width,lb[6].height,lb[6].x,lb[6].y,mousePos,mouseState):
            q = checker(keys,kojih)
            if q==32:
                lb[6].text_surface = myfont1.render(f"Change heal key from Space", True, (15, 15, 15))
            if q>=33 and q<=126:
                kojih=q
                lb[6].text_surface = myfont1.render(f"Change heal key from {char[kojih-34]}", True, (15, 15, 15))
    
    

    
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||
    if prozor==0:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                write(info)
                exit()
        if keys[pygame.K_ESCAPE]:
            if washolding==False:
                write(info)
                exit()
        else:
            washolding=False
        e = random.randint(1,10)
        if e == 1:
            w = random.randint(2,5)
            e = random.randint(10,728)
            l_b.append(Background(e,w))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==0:
                lb[i].draw(window)
        if button_colision(lb[0].width,lb[0].height,lb[0].x,lb[0].y,mousePos,mouseState):
            prozor=1
        if button_colision(lb[1].width,lb[1].height,lb[1].x,lb[1].y,mousePos,mouseState):
            prozor=2
        if button_colision(lb[2].width,lb[2].height,lb[2].x,lb[2].y,mousePos,mouseState):
            prozor=3
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    if prozor==1:
        keys = pygame.key.get_pressed()
        levo =keys[kojil]
        desno=keys[kojid]
        pucaj=keys[kojis]
        heluj=keys[kojih]
        keydict["left"]=levo
        keydict["right"]=desno
        keydict["shot"]=pucaj
        keydict["heal"]=heluj
        a_r = random.randint(1,20)
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
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                l_a,l_l,prozor,l_e,l_m = mainmenu()
                
        if keys[pygame.K_ESCAPE]:
            l_a,l_l,prozor,l_e,l_m = mainmenu()
            washolding=True
        if p1.health==0:
            l_a,l_l,prozor,l_e,l_m = mainmenu()
        draw_minerals(25,25,window,minerala)
        
        
            
        #laser
        q = 0
        for i in range(len(l_l)):
            if l_l[q].health == 0:
                del l_l[q]
                q-=1
            q+=1
        r = 0

        if keydict["shot"]:
            if p1.time <= 0:
                p1.time =10
                if len(l_l) == 100:
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
        if keydict["heal"]:
            if p1.health<=2:
                if minerala>=35:
                    p1.health+=1
                    minerala-=35
                
        for i in range(len(l_b)):
            if l_b[r].y >= 765:
                del l_b[r]
                r-=1
            r+=1
        
        #asteroids
        for i in range(len(l_a)):
            if l_a[i].strana==0:
                l_a[i].draw(window)
        r = 0
        for i in range(len(l_a)):
            if l_a[r].y >= 765:
                del l_a[r]
                r-=1
            r+=1
            
        err = 0
        for i in range(len(l_a)):
            if p1.health!=1:
                if colision1(pygame.Rect(p1.x+30,p1.y,p1.width-60,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                    p1.health-=1
                    l_a[err].alive=False
                    l_a[err].drop=False
            else:
                if colision1(pygame.Rect(p1.x,p1.y,p1.width-30,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                    p1.health-=1
                    l_a[err].alive=False
                    l_a[err].drop=False
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
                if l_a[err].drop==True:
                    m = Mineral(l_a[err].x,l_a[err].y,2.5)
                    l_m.append(m)
                for i in range(5):
                    timeSpread = i*5
                    scaleSpread = 1.8-(i/10)*2
                    e = Explosion(random.randint(l_a[err].x-30,l_a[err].x+l_a[err].width-10),random.randint(l_a[err].y-30,l_a[err].y+l_a[err].height-10),l_a[err].width,l_a[err].height,timeSpread,scaleSpread)
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
                l_m[i].alive = False
                
        err = 0
        for i in range(len(l_m)):
            if l_m[err].alive == False:
                del l_m[err]
                err-=1
            err+=1
            
        p1.draw(window)
        p1.move(keydict)
        #asteroids
        for i in range(len(l_a)):
            if l_a[i].strana==1:
                l_a[i].draw(window)
        r = 0
        for i in range(len(l_a)):
            if l_a[r].y >= 765:
                del l_a[r]
                r-=1
            r+=1
    pygame.display.update()
    clock.tick(60)