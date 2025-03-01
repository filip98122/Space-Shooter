import os
import pygame
import random
import math
import time
import json
from cryptography.fernet import Fernet
pygame.init()
pygame.mixer.init()
keys = pygame.key.get_pressed()
keyE = b'nL5cTPi0324Gk2zgRDR6E4Y2iVHfWnrKu4kGzcB1ZnU='

def ens(file_data):
    f=Fernet(keyE)
    encrypted_data1=json.dumps(file_data).encode('utf-8')
    encrypted_data = f.encrypt(encrypted_data1)
    with open("infojson.json", "wb") as file:
        file.write(encrypted_data)


def end():
    f=Fernet(keyE)
    with open("infojson.json", "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_data1=json.loads(decrypted_data.decode('utf-8'))
    return decrypted_data1

def Vector_Normalization(x1, y1, x2, y2):
    # Calculate dx and dy with direction
    distancex = x2 - x1
    distancey = y2 - y1
    vector_lenght=math.sqrt(distancex*distancex+distancey*distancey)
    distancex=distancex/vector_lenght
    distancey=distancey/vector_lenght
    distancex*=HEIGHT/150
    distancey*=HEIGHT/150                                                                                                                                                                        
    return distancex,distancey

    
    
    
    
    



def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def collision1(rect1 : pygame.Rect,rect2):
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
    if pressed!=0 and pressed!=kojih and pressed!=kojis and pressed!=kojid and pressed!=kojil and pressed!=kojig and pressed!=kojidole:
        return pressed
    else:
        return index

keydict={
    "shot":keys[pygame.K_SPACE],
    "left":keys[pygame.K_a],
    "right":keys[pygame.K_d],
    "heal":keys[pygame.K_h],
    "up":keys[pygame.K_w],
    "down":keys[pygame.K_s]
}
clock = pygame.time.Clock()
WIDTH,HEIGHT = 1540,900
window = pygame.display.set_mode((WIDTH,HEIGHT))
def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    """Collides the clicking of the would-be button given"""
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

class Background:
    """Moves and draws the background"""
    def __init__(s,x):
        s.x = x
        s.y = 0
        s.scale = 9
        s.d = random.randint(1,5)
        s.speedy=(HEIGHT/765)*s.d
        if s.d == 5:
            s.image = pygame.image.load('star1.png')
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d <= 3:
            s.image = pygame.image.load('star3.png')
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d == 4:
            s.image = pygame.image.load('star2.png')
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.speedy==1:
            s.speedy+=1
    def move_and_draw(s,window):
        s.y+=s.speedy
        window.blit(s.scaled_img,(s.x,s.y))
l_b = []
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
        scale=1
        s.img = pygame.image.load('1c.png')
        s.height = int(int(HEIGHT/11.25)*scale)
        s.width = s.height
        e=pygame.transform.scale(s.img, (s.width, s.height))
        
        
        s.img = pygame.image.load('2.png')
        s.width = s.img.get_width()*s.scale
        s.height = int(int(HEIGHT/11.25)*scale)
        s.width = s.height
        w=pygame.transform.scale(s.img, (s.width, s.height))
        
        
        
        s.img = pygame.image.load('3.png')
        s.width = s.img.get_width()*s.scale
        s.height = int(int(HEIGHT/11.25)*scale)
        s.width=s.height
        q=pygame.transform.scale(s.img, (s.width, s.height))
        
        s.img = pygame.image.load('1l.png')
        s.width = s.img.get_width()*s.scale
        s.height = int(int(HEIGHT/11.25)*scale)
        s.width=s.height
        t=pygame.transform.scale(s.img, (s.width, s.height))
        
        s.img = pygame.image.load('1r.png')
        s.width = s.img.get_width()*s.scale
        s.height = int(int(HEIGHT/11.25)*scale)
        s.width=s.height
        r=pygame.transform.scale(s.img, (s.width, s.height))
        s.str=""
        
        
        s.dict={
            3:q,
            2:w,
            "1c":e,
            "1l":t,
            "1r":r
            
        }
        

        
    def draw(self,window):
        if self.health<=0:
            return
        else:
            if self.health!=1:
                self.width=self.dict[self.health].get_width()
                self.height=self.dict[self.health].get_height()
                window.blit(self.dict[self.health],(self.x,self.y))
            else:
                self.width=self.dict[f'{self.health}{self.str}'].get_width()
                self.height=self.dict[f'{self.health}{self.str}'].get_height()
                window.blit(self.dict[f'{self.health}{self.str}'],(self.x,self.y))
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

class Particle:
    def __init__(s,x,y,lifetime,dx,dy):
        s.x=x
        s.y=y
        s.lifetime=lifetime
        s.dx=dx
        s.dy=dy
        s.distancex=0
        s.distancey=0
        s.distance=0
        s.radius=HEIGHT/(16.6304347826087*5)
        s.color = (random.randint(118, 138), random.randint(0, 20), random.randint(118, 138))
        s.alpha = random.randint(50, 100)
    def draw(self, screen):
        particle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA) #Create transparent surface.
        pygame.draw.circle(particle_surface, self.color + (self.alpha,), (self.radius, self.radius), self.radius) #draw circle with alpha.
        screen.blit(particle_surface, (int(self.x - self.radius), int(self.y - self.radius))) # blit surface to main screen.
        self.alpha-=0.1
        self.alpha = max(0, self.alpha) # Example of decreasing alpha over time.
class Particle_System:
    """Updates every partcle movment"""
    def __init__(s):
        s.l_p=[]
        s.gravity=0.08
        s.attractor=0
    def draw(s,window):
        for i in range(len(s.l_p)):
            s.l_p[i].draw(window)
    
    
    def update(s):
        # Spawn new particles if needed
        probpart=random.randint(1,3)
        if probpart==1:
            w=random.randint(1,3)
            qqq=random.randint(1,2)
            if qqq==1:
                w*=-1
            s.l_p.append(Particle(WIDTH/2+WIDTH/2.566666666666667,HEIGHT/2-WIDTH/5.133333333333333,250,w,-10))
        
        
        count=0
        for i in range(len(s.l_p)):
            if s.l_p[count].lifetime<=0:
                del s.l_p[count]
                count-=1
            count+=1
        
        # Movement
        for i in range(len(l_attractors)):
            if l_attractors[i].prozor==prozor:
                for j in range(len(s.l_p)):
                    s.l_p[j].distancex=l_attractors[i].x-s.l_p[j].x
                    s.l_p[j].distancey=l_attractors[i].y-s.l_p[j].y
                    s.l_p[j].distance=math.sqrt(s.l_p[j].distancex*s.l_p[j].distancex+s.l_p[j].distancey*s.l_p[j].distancey)
                    s.l_p[j].dx+=(s.l_p[j].distancex*(HEIGHT/1092857.142857143))
                    s.l_p[j].dy+=(s.l_p[j].distancey*(HEIGHT/1092857.142857143))
                #l_attractors[i].draw(window)
                if s.attractor==0:
                    """
                    for ii in range(len(l_attractors)):
                        l_attractors[ii].x=random.randint(0,WIDTH)
                        l_attractors[ii].y=random.randint(0,HEIGHT)
                    """
                    s.attractor=240
        for i in range(len(s.l_p)):
            if s.l_p[i].lifetime>=1:
                s.l_p[i].dy+=s.gravity
                s.l_p[i].x+=s.l_p[i].dx
                s.l_p[i].y+=s.l_p[i].dy
                
                s.l_p[i].lifetime-=1
        s.attractor-=1


class Attractor:
    def __init__(s,x,y,prozor):
        s.x=x
        s.y=y
        s.prozor=prozor
        s.img = pygame.image.load("particle_red.png")
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.x+=s.width/2
        s.y+=s.height/2
    def draw(s,window):
        window.blit(s.scaled_img,(s.x-s.width/2,s.y-s.height/2))
l_attractors=[Attractor(WIDTH/2,HEIGHT/2,0),
              Attractor(WIDTH/2,HEIGHT/2,0)
              
              
              
              
              
              
              
              
              
              
]
#l_attractors=[]

part=Particle_System()





class Missle:
    def __init__(s,x):
        s.x=x
        s.y=p1.y
        s.angle=0
        s.img = pygame.image.load("particle.png")
        s.width = 336*0.075
        s.height = 801*0.075
        s.minbrzina=-3
        s.maxbrzina=4
        s.index=-1
        s.dx=0
        s.dy=-2
        s.ddx=0
        s.ddy=0
        s.alive=True
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.q=0.0075
        mindistince=1000000
        s.y-=s.height
        for i in range(len(l_a)):
            if l_a[i].alive==True:
                delx=l_a[i].x-s.x
                dely=l_a[i].y-s.y
                distince=math.sqrt(delx*delx+dely*dely)
                if distince<mindistince:
                    mindistince=distince
                    s.index=i
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
    def draw(s,window):
        rotated_img=pygame.transform.rotate(s.scaled_img,s.angle)
        s.width=rotated_img.get_width()
        s.height=rotated_img.get_height()
        window.blit(rotated_img,(s.x,s.y))
    def move(s):
        if s.index>=0 and s.index <len(l_a):
            if l_a[s.index].x<s.x:
                s.ddx-=s.q
            elif l_a[s.index].x!=s.x:
                s.ddx+=s.q
            if l_a[s.index].y<s.y:
                s.ddy-=s.q
            elif l_a[s.index].y!=s.y:
                s.ddy+=s.q
        s.dx+=s.ddx
        s.dy+=s.ddy
        s.x+=s.dx
        s.y+=s.dy
        if s.x+s.width<0 or s.x>WIDTH or s.y+s.height<0 or s.y>HEIGHT:
            s.alive=False
            
    def change(s):
        s.index=-1
        mindistince=1000000
        for i in range(len(l_a)):
            if l_a[i].alive==True:
                delx=l_a[i].x-s.x
                dely=l_a[i].y-s.y
                distince=math.sqrt(delx*delx+dely*dely)
                if distince<mindistince:
                    mindistince=distince
                    s.index=i




class Mineral:
    def __init__(s,x,y,dy):
        s.x = x
        s.y = y
        s.alive = True
        s.dy = dy
        s.img = pygame.image.load("mineral.png")
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
    def move_and_draw(s,window):
        if s.alive == True:
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))
            if s.y >= HEIGHT:
                s.alive = False

class Green_Mineral:
    def __init__(s,x,y,dy):
        s.x = x
        s.y = y
        s.alive = True
        s.dy = dy
        s.img = pygame.image.load("green mineral.png")
        s.width = HEIGHT/25.5
        s.height = HEIGHT/25.5
        s.scaled_img = pygame.transform.scale(s.img, (s.width, s.height))
        s.x-=s.width/2
    def move_and_draw(s,window):
        global whenwin
        if s.alive == True:
            s.y+=s.dy
            window.blit(s.scaled_img,(s.x,s.y))
            if s.y >= HEIGHT:
                s.alive = False
                whenwin=300



l_m = []
class Asteroid:
    def __init__(s,x,y,alive):
        s.x = x
        s.y = y
        s.drop=True
        s.strana=random.randint(0,1)
        s.alive =alive
        s.Time_from_death = 70
        s.img_choice = random.randint(1,4)
        s.speed = random.randint(int(HEIGHT/382.5),int(HEIGHT/153))
        if s.img_choice == 1:
            s.image = pygame.image.load("asteroid1.png")
        if s.img_choice == 2:
            s.image = pygame.image.load("asteroid2.png")
        if s.img_choice == 3:
            s.image = pygame.image.load("asteroid3.png")
        if s.img_choice == 4:
            s.image = pygame.image.load("asteroid4.png")
            
        
        s.height = int(HEIGHT/16.6304347826087)
        s.width = int(HEIGHT/16.6304347826087)
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def draw(s,window):
        if s.alive >= 0:
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

class Rotated_Laser:
    def __init__(self,x,y,angle,health,str=None):
        self.x=x
        self.y=y
        self.health=health
        self.angle=angle
        self.scale=0.3*0.75
        self.dy=-HEIGHT/109.2857142857143
        self.ddy=-HEIGHT/15300
        self.img = pygame.image.load('laser.png')
        self.width = self.img.get_width()*(HEIGHT/3400)
        self.height = self.img.get_height()*(HEIGHT/3400)
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
        if self.angle==45:
            self.dx=-HEIGHT/109.2857142857143
            self.ddx=-HEIGHT/15300
        else:
            self.dx=HEIGHT/109.2857142857143
            self.ddx=HEIGHT/15300
        self.rotated_img=pygame.transform.rotate(self.scaled_img,self.angle)
        if p1.power_db>0:
            if str==2:
                self.y-=l_l[len(l_l)-1].width/2
            else:
                self.y+=l_l[len(l_l)-1].width/2
    def move_and_draw(s,window):
        window.blit(s.rotated_img,(s.x,s.y))
        s.x+=s.dx
        s.dx+=s.ddx
        s.y+=s.dy
        s.dy+=s.ddy
        if s.x+s.width<=0 or s.x>WIDTH:
            s.health=0


class Power_up_db:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.speed=HEIGHT/306
        s.alive=True
        s.image=pygame.image.load("powerupdb.png")
        s.height = HEIGHT/17
        s.width = HEIGHT/17
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def move_and_draw(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.y+=s.speed
        if s.y>=HEIGHT:
            s.alive=False
l_lr=[]



class Power_up_rb:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.speed=HEIGHT/306
        s.alive=True
        s.image=pygame.image.load("poweruprb.png")
        s.height = HEIGHT/17
        s.width = HEIGHT/17
        s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
    def move_and_draw(s,window):
        s.y+=s.speed
        window.blit(s.scaled_img,(s.x,s.y))
        if s.y>=HEIGHT:
            s.alive=False

class Laser:
    def __init__(self,x,health,str=None):
        self.x = x
        self.y = p1.y
        self.health = health
        self.scale = 0.3*0.75
        self.dy=-HEIGHT/109.2857142857143
        self.ddy=-HEIGHT/15300
        self.img = pygame.image.load('laser.png')
        self.width = self.img.get_width()*(HEIGHT/3400)
        self.height = self.img.get_height()*(HEIGHT/3400)
        self.scaled_img = pygame.transform.scale(self.img, (self.width, self.height))
        self.y-=self.height
        if p1.power_db>0:
            if str==1:
                self.x-=self.width
        else:
            self.x-=self.width/2
    def draw(s,window):
        if s.health >0:
            if s.y <= -53*0.75:
                s.health =0
            s.y+=s.dy
            s.dy+=s.ddy
            window.blit(s.scaled_img,(s.x,s.y))

class Button:
    def __init__(self,x,y,img,text,font,prozor,scale,scale1):
        self.x=x
        self.y=y
        self.scale=2.8
        self.scale=scale
        self.scale1=scale1
        self.prozor = prozor
        self.text=text
        img1=pygame.image.load(f"{img}.png")
        self.width=img1.get_width()*self.scale
        self.height=img1.get_height()*self.scale1
        self.scaled_img=pygame.transform.scale(img1,(self.width,self.height))
        self.x-=self.width/2
        self.y-=self.height/2
        if text!="":
            self.text_surface = font.render(f"{text}", True, (15, 15, 15))
            self.width1=self.text_surface.get_width()
            self.height1=self.text_surface.get_height()
            self.x1=self.x+((self.width-self.width1)//2)
            self.y1=self.y+((self.height-self.height1)//2)
    def draw(self,window):
        window.blit(self.scaled_img,(self.x,self.y))
        if self.text!="":
            window.blit(self.text_surface,(self.x1,self.y1))


class Boss:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.scale=HEIGHT/900
        img1=pygame.image.load(f"boss.png")
        s.width=img1.get_width()*s.scale
        s.height=img1.get_height()*s.scale
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.shoot=0
        s.x-=s.width/2
        s.health = 75
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        if s.shoot==0:
            s.make_fireball()
            s.shoot=50
        else:
            s.shoot-=1
    def make_fireball(s):
        l_f.append(Fireball(s.x+s.width/2,s.y+s.height))
        
l_f=[]

class Fireball:
    def __init__(s,x,y):
        s.health=1
        s.x=x
        s.y=y
        s.scale=HEIGHT/1800
        img1=pygame.image.load(f"fireball.png")
        s.width=img1.get_width()*s.scale
        s.height=img1.get_height()*s.scale
        s.scaled_img=pygame.transform.scale(img1,(s.width,s.height))
        s.dx,s.dy=Vector_Normalization(s.x+s.width/2,s.y+s.height/2,p1.x+p1.width/2,p1.y+p1.height/2)
        s.x-=s.width/2
    def general(s,window):
        window.blit(s.scaled_img,(s.x,s.y))
        s.x+=s.dx
        s.y+=s.dy
        if s.x+s.width<=0 or s.x>=WIDTH or s.y>=HEIGHT or s.y+s.height<=0:
            s.health=0




boss = Boss(WIDTH/2,100)




l_l = []
start=50
def mainmenu():
    global ukupnom
    global minerala
    global l_lr
    global l_prb
    global l_pdb
    global boss
    boss = Boss(WIDTH/2,100)
    global l_f
    l_f=[]
    global l_missle
    l_missle=[]
    l_pdb=[]
    global p1
    p1.power_db=0
    p1.power_rb=0
    p1.str=""
    l_prb=[]
    l_lr=[]
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
    info=end()
    return info

info=read()

def write(info):
    info["minerala"]=ukupnom
    info["minerala"]=0
    ens(info)


SCALE_MAIN_MENU_BUTTON=273.2142857142857
SCALE_SETTINGS_BUTTON=127.5

wsmmb=WIDTH/SCALE_MAIN_MENU_BUTTON
hsmmb=HEIGHT/SCALE_MAIN_MENU_BUTTON
wssb=WIDTH/SCALE_SETTINGS_BUTTON
hssb=HEIGHT/SCALE_SETTINGS_BUTTON





myfont1 = pygame.font.SysFont('s', int(HEIGHT/12.75))

p1 = Player(100,550,0,0,WIDTH/160)

myfont = pygame.font.SysFont('s', int(HEIGHT/10.92857142857143))

lb=[Button(WIDTH/2,HEIGHT/4,"start","",0,0,wsmmb,hsmmb),
    Button(WIDTH/2,2*(HEIGHT/4),"settings","",0,0,wsmmb,hsmmb),
    Button(WIDTH/2,3*(HEIGHT/4),"shop","",0,0,wsmmb,hsmmb),
    Button(WIDTH/2,HEIGHT/6*1,"zapucanje","Change shoot key from Space",myfont1,3,wssb,hssb),
    Button(WIDTH/2,HEIGHT/6*2,"zapucanje","Change go left key from a",myfont1,3,wssb,hssb),
    Button(WIDTH/2,HEIGHT/6*3,"zapucanje","Change go right key from d",myfont1,3,wssb,hssb),
    Button(WIDTH/2,HEIGHT/6*4,"zapucanje","Change heal key from h",myfont1,3,wssb,hssb),
    Button(WIDTH/2,HEIGHT/6*1,"zapucanje","Change go up key from w",myfont1,4,wssb,hssb),
    Button(WIDTH/2,HEIGHT/6*2,"zapucanje","Change go down key from s",myfont1,4,wssb,hssb)
]
def draw_minerals(x,y,window,minerala):
    img = pygame.image.load("mineral.png")
    width = HEIGHT/25.5
    height = HEIGHT/25.5
    scaled_img = pygame.transform.scale(img, (width, height))
    window.blit(scaled_img,(x,y))
    myfont = pygame.font.SysFont('B', int(HEIGHT/17))
    text_surface = myfont.render(f"{minerala}", True, (255, 255, 255))
    window.blit(text_surface,(x+width+WIDTH/76.5,y))


def prom(index):
    lb[index].width1=lb[index].text_surface.get_width()
    lb[index].height1=lb[index].text_surface.get_height()
najvecivreme=0

class Store:
    def __init__(s,x,y,index,text,cost,quantity,op):
        s.x =x
        s.y=y
        s.quantity=quantity
        s.index=index
        s.op=op
        s.cost=cost
        s.img = pygame.image.load("buttons.png")
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

l_s=[
    Store(WIDTH/7.65,HEIGHT/7.65,"fire rate","Laser exhaust",100,7,-1),
    Store(WIDTH/7.65,(HEIGHT/7.65)*2,"damage","Laser damage",100,5,1)
    
    
    
    
    
    
]
kojidole=info["kojidole"]
kojig=info["kojig"]
kojis=info["kojis"]
kojil=info["kojil"]
kojid=info["kojid"]
kojih=info["kojih"]
q=kojis
if q==32:
    info["kojis"]=q
    kojis=q
    lb[3].text_surface = myfont1.render(f"Change shoot key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojis"]=q
    kojis=q
    lb[3].text_surface = myfont1.render(f"Change shoot key from {char[kojis-34]}", True, (15, 15, 15))













#zakasnije
















q=kojig
if q==32:
    info["kojig"]=q
    kojig=q
    lb[7].text_surface = myfont1.render(f"Change go up key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojig"]=q
    kojig=q
    lb[7].text_surface = myfont1.render(f"Change go up key from {char[kojig-34]}", True, (15, 15, 15))

q=kojidole
if q==32:
    info["kojidole"]=q
    kojidole=q
    lb[8].text_surface = myfont1.render(f"Change go down key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojidole"]=q
    kojidole=q
    lb[8].text_surface = myfont1.render(f"Change go down key from {char[kojidole-34]}", True, (15, 15, 15))





SVAKIH30=0
vremep=time.time()
myfontwin = pygame.font.SysFont('s', int(HEIGHT/9))
text_surfacewin = myfontwin.render(f"You win!", True, (255,255,255))
widthwin=text_surfacewin.get_width()
heightwin=text_surfacewin.get_height()
def win():
    window.blit(text_surfacewin,(WIDTH/2-widthwin/2,HEIGHT/9))





buttonscrolltimes=1
buttonscrollloc=0
def button_scroll():
    window.blit(imgs,(x,y))
    window.blit(text_surface,(x1,y1))
    #WIDTH/2,HEIGHT/6*5.5

img=pygame.image.load("buttons.png")
text_surface = myfont1.render(f"Next page", True, (0,0,0))
width=lb[3].width
height=lb[3].height
width1=text_surface.get_width()
height1=text_surface.get_height()
imgs=pygame.transform.scale(img,(width,height))
qqqqqqqq=1
x,y=WIDTH/2-width/2,lb[6].y+lb[6].height
x1,y1=WIDTH/2-width1/2,lb[6].y+lb[6].height+height/2-height1/2







whenwin=0










l_missle=[]


q=kojil
if q==32:
    kojil=q
    info["kojil"]=q
    lb[4].text_surface = myfont1.render(f"Change go left key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    kojil=q
    info["kojil"]=q
    lb[4].text_surface = myfont1.render(f"Change go left key from {char[kojil-34]}", True, (15, 15, 15))


q=kojid
if q==32:
    kojid=q
    info["kojid"]=q
    lb[5].text_surface = myfont1.render(f"Change sgo right key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    kojid=q
    info["kojid"]=q
    lb[5].text_surface = myfont1.render(f"Change go right key from {char[kojid-34]}", True, (15, 15, 15))
button_scrollhold=False

l_pdb=[]
l_prb=[]
q=kojih
if q==32:
    kojih=q
    info["kojih"]=q
    lb[6].text_surface = myfont1.render(f"Change heal key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    kojih=q
    info["kojih"]=q
    lb[6].text_surface = myfont1.render(f"Change heal key from {char[kojih-34]}", True, (15, 15, 15))
prom(3)
prom(4)
prom(5)
prom(6)
prom(7)
prom(8)
e2=int(14780/WIDTH)
qq=1
ukupnom=info["minerala"]
minerala = 0
prozor=0
washolding=False
vremepre=time.time()
while True:
    vremep=time.time()
    if prozor==-1:
        if qq==1:
            qq=0
            aaa=info["highscore"]
            font=pygame.sysfont.SysFont("B",45)
            font1=pygame.sysfont.SysFont("B",75)
            font2=pygame.sysfont.SysFont("B",100)
            txts= font1.render(f"Minerals: {minerala}", True, (255, 255, 255))
            txtsw=txts.get_width()
            txts1= font.render(f"Highscore: {aaa}", True,  (255, 255, 255))
            txtsw2=txts.get_width()
            txts2= font2.render(f"You died!", True,  (255, 255, 255))
            txtsw1=txts1.get_width()
        
        window.fill("Black")
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        window.blit(txts2,(WIDTH//2-txtsw2//2,100))
        window.blit(txts1,(WIDTH//2-txtsw1//2,410))
        window.blit(txts,(WIDTH//2-txtsw//2,300))
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                prozor=0
                qq=1
                l_a,l_l,prozor,l_e,l_m=mainmenu()
        if keys[pygame.K_ESCAPE]:
            if washolding==False:
                prozor=0
                qq=1
                l_a,l_l,prozor,l_e,l_m=mainmenu()
                washolding=True
        else:
            washolding=False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
#STORE CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||||
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
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==2:
                lb[i].draw(window)
        for i in range(len(l_s)):
            l_s[i].draw(window)
            if button_colision(l_s[i].width,l_s[i].height,l_s[i].x,l_s[i].y,mousePos,mouseState):
                if ukupnom>=l_s[i].cost:
                    if l_s[i].op<0:
                        if l_s[i].quantity<info[l_s[i].index]:
                            ukupnom-=l_s[i].cost
                            info[l_s[i].index]+=l_s[i].op
                    else:
                        if l_s[i].quantity>info[l_s[i].index]:
                            ukupnom-=l_s[i].cost
                            info[l_s[i].index]+=l_s[i].op
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
#SETTINGS PAGE 2 IS BELOW |||||||||||||||||||||||||||||||||||||||||
    if prozor==4:
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
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==4:
                lb[i].draw(window)
        button_scroll()
        if button_colision(width,height,WIDTH/2-width/2,lb[6].y+lb[6].height,mousePos,mouseState):
            if button_scrollhold==False:
                prozor+=1
                buttonscrollloc+=1
                button_scrollhold=True
        else:
            button_scrollhold=False
        if buttonscrollloc>buttonscrolltimes:
            prozor=3
            buttonscrollloc=0
        if buttonscrollloc<0:
            prozor=3+buttonscrolltimes

        #GO UP CODE IS BELOW ||||||||||||||||||||||||||||||||||||||
        #GO UP CODE IS BELOW ||||||||||||||||||||||||||||||||||||||
        #GO UP CODE IS BELOW ||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[7].width,lb[7].height,lb[7].x,lb[7].y,mousePos,mouseState):
            q = checker(keys,kojig)
            if q==32:
                info["kojig"]=q
                kojig=q
                lb[7].text_surface = myfont1.render(f"Change go up key from Space", True, (15, 15, 15))
                prom(7)
            if q>=33 and q<=126:
                info["kojig"]=q
                kojig=q
                lb[7].text_surface = myfont1.render(f"Change go up key from {char[kojig-34]}", True, (15, 15, 15))
                prom(7)
        
        #GO DOWN CODE IS BELOW ||||||||||||||||||||||||||||||||||||
        #GO DOWN CODE IS BELOW ||||||||||||||||||||||||||||||||||||
        #GO DOWN CODE IS BELOW ||||||||||||||||||||||||||||||||||||
        if button_colision(lb[8].width,lb[8].height,lb[8].x,lb[8].y,mousePos,mouseState):
            q = checker(keys,kojidole)
            if q==32:
                info["kojidole"]=q
                kojidole=q
                lb[8].text_surface = myfont1.render(f"Change go up key from Space", True, (15, 15, 15))
                prom(8)
            if q>=33 and q<=126:
                info["kojidole"]=q
                kojidole=q
                lb[8].text_surface = myfont1.render(f"Change go up key from {char[kojidole-34]}", True, (15, 15, 15))
                prom(8)
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||
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
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
            
        for i in range(len(lb)):
            if lb[i].prozor==3:
                lb[i].draw(window)
            
        button_scroll()
        if button_colision(width,height,WIDTH/2-width/2,lb[6].y+lb[6].height,mousePos,mouseState):
            if button_scrollhold==False:
                prozor+=1
                buttonscrollloc+=1
                button_scrollhold=True
                if buttonscrollloc>buttonscrolltimes:
                    prozor=3
                    buttonscrollloc=0
                if buttonscrollloc<0:
                    prozor=3+buttonscrolltimes
        else:
            if button_scrollhold==True:
                button_scrollhold=False
    #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
    #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
    #SHOOT CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[3].width,lb[3].height,lb[3].x,lb[3].y,mousePos,mouseState):
            q = checker(keys,kojis)
            if q==32:
                info["kojis"]=q
                kojis=q
                lb[3].text_surface = myfont1.render(f"Change shoot key from Space", True, (15, 15, 15))
                prom(3)
            if q>=33 and q<=126:
                info["kojis"]=q
                kojis=q
                lb[3].text_surface = myfont1.render(f"Change shoot key from {char[kojis-34]}", True, (15, 15, 15))
                prom(3)
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[4].width,lb[4].height,lb[4].x,lb[4].y,mousePos,mouseState):
            q = checker(keys,kojil)
            if q==32:
                kojil=q
                info["kojil"]=q
                lb[4].text_surface = myfont1.render(f"Change go left key from Space", True, (15, 15, 15))
                prom(4)
            if q>=33 and q<=126:
                kojil=q
                info["kojil"]=q
                lb[4].text_surface = myfont1.render(f"Change go left key from {char[kojil-34]}", True, (15, 15, 15))
                prom(4)
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[5].width,lb[5].height,lb[5].x,lb[5].y,mousePos,mouseState):
            q = checker(keys,kojid)
            if q==32:
                kojid=q
                info["kojid"]=q
                lb[5].text_surface = myfont1.render(f"Change go right key from Space", True, (15, 15, 15))
                prom(5)
            if q>=33 and q<=126:
                kojid=q
                info["kojid"]=q
                lb[5].text_surface = myfont1.render(f"Change go right key from {char[kojid-34]}", True, (15, 15, 15))
                prom(5)
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[6].width,lb[6].height,lb[6].x,lb[6].y,mousePos,mouseState):
            q = checker(keys,kojih)
            if q==32:
                kojih=q
                info["kojih"]=q
                lb[6].text_surface = myfont1.render(f"Change heal key from Space", True, (15, 15, 15))
                prom(6)
            if q>=33 and q<=126:
                kojih=q
                info["kojih"]=q
                lb[6].text_surface = myfont1.render(f"Change heal key from {char[kojih-34]}", True, (15, 15, 15))
                prom(6)
    

        
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    #MAIN MENU CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
    if prozor==0:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                write(info)
                ens(info)
                print(najvecivreme)
                print(30/najvecivreme)
                exit()
        if keys[pygame.K_ESCAPE]:
            if washolding==False:
                write(info)
                ens(info)
                print(najvecivreme)
                print(30/najvecivreme)
                exit()
        else:
            washolding=False
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        window.fill("Black")
        part.draw(window)
        part.update()
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==0:
                lb[i].draw(window)
        if button_colision(lb[0].width,lb[0].height,lb[0].x,lb[0].y,mousePos,mouseState):
            prozor=1
        if button_colision(lb[1].width,lb[1].height,lb[1].x,lb[1].y,mousePos,mouseState):
            prozor=3
        if button_colision(lb[2].width,lb[2].height,lb[2].x,lb[2].y,mousePos,mouseState):
            prozor=2
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    if prozor==1:
        if info["fire rate"]<7:
            info["fire rate"]=7
        keys = pygame.key.get_pressed()
        levo =keys[kojil]
        desno=keys[kojid]
        pucaj=keys[kojis]
        heluj=keys[kojih]
        gore=keys[kojig]
        dole=keys[kojidole]
        keydict["left"]=levo
        keydict["right"]=desno
        keydict["shot"]=pucaj
        keydict["heal"]=heluj
        keydict["up"]=gore
        keydict["down"]=dole
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if boss.health>0:
            a_r = random.randint(1,int(14800/WIDTH))
        if a_r == 1:
            ast = Asteroid(random.randint(0,WIDTH-int(HEIGHT/16.6304347826087)),-int((HEIGHT/16.6304347826087)+10),info['asteroid health'])
            l_a.append(ast)
        e = random.randint(1,e2)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_b.append(Background(e))
        window.fill("Black")
        for i in range(len(l_b)):
            l_b[i].move_and_draw(window)
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                if info["highscore"]<minerala:
                    info["highscore"]=minerala
                l_a,l_l,prozor,l_e,l_m=mainmenu()
        
              
        if keys[pygame.K_ESCAPE]:
            prozor=0
            if info["highscore"]<minerala:
                info["highscore"]=minerala
            l_a,l_l,prozor,l_e,l_m=mainmenu()
            washolding=True
        if p1.health==0:
            prozor=-1
            if info["highscore"]<minerala:
                info["highscore"]=minerala
        draw_minerals(HEIGHT/30.6,HEIGHT/30.6,window,minerala)
        
        
            
        #laser
        q = 0
        for i in range(len(l_l)):
            if l_l[q].health <= 0:
                del l_l[q]
                q-=1
            q+=1
        r = 0
        q=0
        for i in range(len(l_lr)):
            if l_lr[q].health <= 0:
                del l_lr[q]
                q-=1
            q+=1
        if boss.health>0 or len(l_a)>0:
            if keydict["shot"]:
                if p1.time_missle<=0:
                    l_missle.append(Missle(p1.x+p1.width/2))
                    p1.time_missle=info["fire rate missle"]
                if p1.time <= 0:
                    l1 = Laser(p1.x+p1.width/2,info["damage"])
                    if p1.power_db>0:
                        l2=Laser(p1.x+p1.width/2,info["damage"],1)
                        l_l.append(l2)
                    p1.time = info["fire rate"]
                    l_l.append(l1)
                    if p1.power_rb>0:
                        if p1.power_db==0:
                            if p1.str=="r" or p1.str=="" or p1.str=="c":
                                l1r=Rotated_Laser(p1.x-p1.width/12.9,p1.y-(p1.height/11.9)*2,45,info["damage"])
                                l_lr.append(l1r)
                            if p1.str=="l" or p1.str=="" or p1.str=="c":
                                l1r=Rotated_Laser(p1.x+(p1.width/12.9)*9,p1.y-(p1.height/11.9)*2,315,info["damage"])
                                l_lr.append(l1r)
                        else:
                            if p1.str=="r" or p1.str=="" or p1.str=="c":
                                l1r=Rotated_Laser(p1.x-p1.width/12.9,(p1.y-(p1.height/11.9)*2)        ,45,info["damage"],1)
                                l_lr.append(l1r)
                                l1r=Rotated_Laser(p1.x-p1.width/12.9,(p1.y-(p1.height/11.9)*2)        ,45,info["damage"],2)
                                l_lr.append(l1r)
                            if p1.str=="l" or p1.str=="" or p1.str=="c":
                                l1r=Rotated_Laser(p1.x+(p1.width/12.9)*9,(p1.y-(p1.height/11.9)*2)       ,315,info["damage"],1)
                                l_lr.append(l1r)
                                l1r=Rotated_Laser(p1.x+(p1.width/12.9)*9,(p1.y-(p1.height/11.9)*2)       ,315,info["damage"],2)
                                l_lr.append(l1r)

        for i in range(len(l_l)):
            if l_l[i].health != 0:
                l_l[i].draw(window)
        for i in range(len(l_lr)):
            if l_lr[i].health != 0:
                l_lr[i].move_and_draw(window)
        
        #background
        if keydict["heal"]:
            if p1.health<=2:
                if minerala>=35:
                    p1.health+=1
                    minerala-=35
                    if p1.health==2:
                        p1.str=""
                
        for i in range(len(l_b)):
            if l_b[r].y >= HEIGHT:
                del l_b[r]
                r-=1
            r+=1
        
        #asteroids
        for i in range(len(l_a)):
            if l_a[i].strana==0:
                l_a[i].draw(window)
        r = 0
        for i in range(len(l_a)):
            if l_a[r].y >= HEIGHT:
                del l_a[r]
                r-=1
            r+=1
            
        err = 0
        for i in range(len(l_a)):
            if l_a[err].x>=p1.x-l_a[err].width and l_a[err].x<=p1.x+p1.width and l_a[err].y>=p1.y-l_a[err].height and l_a[err].y<=p1.y+p1.height:
                if p1.health!=1:
                    if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                        if p1.health==2:
                            if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                                p1.str="l"
                            elif collision1(pygame.Rect(p1.x+p1.height/2.433962264150943,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                                p1.str="c"
                            else:
                                p1.str="r"
                        
                        p1.health-=1
                        l_a[err].alive=0
                        l_a[err].drop=False
                else:
                    if p1.str=="l":
                        if collision1(pygame.Rect(p1.x,p1.y,p1.width-p1.height/4.3,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                            p1.health-=1 
                            l_a[err].alive=0
                            l_a[err].drop=False
                    elif p1.str=="r":
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                            p1.health-=1
                            l_a[err].alive=0
                            l_a[err].drop=False
                    else:
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_a[err].x,l_a[err].y,l_a[err].width,l_a[err].height)):
                            p1.health-=1
                            l_a[err].alive=0
                            l_a[err].drop=False
            err +=1
        for i in range(len(l_l)):
            for j in range(len(l_a)):
                
                if collision1(pygame.Rect(l_l[i].x,l_l[i].y,l_l[i].width,l_l[i].height),pygame.Rect(l_a[j].x,l_a[j].y,l_a[j].width,l_a[j].height)):         
                    if l_a[j].alive >= 0:
                        l_l[i].health-=1
                        l_a[j].alive-=info['damage']
        for i in range(len(l_lr)):
            for j in range(len(l_a)):
                if collision1(pygame.Rect(l_lr[i].x,l_lr[i].y,l_lr[i].width,l_lr[i].height),pygame.Rect(l_a[j].x,l_a[j].y,l_a[j].width,l_a[j].height)):
                    if l_a[j].alive >= 0:
                        l_lr[i].health-=1
                        l_a[j].alive-=info['damage']
        
        
        
        
        
        for i in range(len(l_missle)):
            for j in range(len(l_a)):
                if collision1(pygame.Rect(l_missle[i].x,l_missle[i].y,l_missle[i].width,l_missle[i].height),pygame.Rect(l_a[j].x,l_a[j].y,l_a[j].width,l_a[j].height)):
                    l_a[j].alive=0
                    l_missle[i].alive=False
        err=0
        for i in range(len(l_missle)):
            if l_missle[err].alive==True:
                l_missle[err].change()
                l_missle[err].move()
                l_missle[err].draw(window)
            else:
                del l_missle[err]
                err-=1
            err+=1
    
        
        
        
        
        
        
        
        
        err = 0
        for i in range(len(l_a)):
            if l_a[err].alive <= 0:
                if l_a[err].drop==True:
                    prob_powerup= random.randint(1,15)
                    if prob_powerup==1:
                        p=Power_up_rb(l_a[err].x,l_a[err].y)
                        l_prb.append(p)
                    elif prob_powerup==2:
                        p=Power_up_db(l_a[err].x,l_a[err].y)
                        l_pdb.append(p)
                    else:
                        m = Mineral(l_a[err].x,l_a[err].y,HEIGHT/306)
                        l_m.append(m)
                for i in range(5):
                    timeSpread = i*5
                    scaleSpread = HEIGHT/425-(i/10)*2
                    e = Explosion(random.randint(int(l_a[err].x-HEIGHT/30),int(l_a[err].x+l_a[err].width-HEIGHT/90)),random.randint(int(l_a[err].y-HEIGHT/30),int(l_a[err].y+l_a[err].height-HEIGHT/90)),l_a[err].width,l_a[err].height,timeSpread,scaleSpread)
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
            if collision1(pygame.Rect(l_m[i].x,l_m[i].y,l_m[i].width,l_m[i].height),pygame.Rect(p1.x,p1.y,p1.width,p1.height)):
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
            if l_a[r].y >= HEIGHT:
                del l_a[r]
                r-=1
            r+=1
        
        
        
        i=0
        for j in range(len(l_pdb)):
            if l_pdb[i].alive==False:
                del l_pdb[i]
                i-=1
            i+=1
        i=0
        for j in range(len(l_pdb)):
            l_pdb[i].move_and_draw(window)
            if collision1(pygame.Rect(l_pdb[i].x,l_pdb[i].y,l_pdb[i].width,l_pdb[i].height),pygame.Rect(p1.x,p1.y,p1.width,p1.height)):
                del l_pdb[i]
                p1.power_db=300
                i-=1
            i+=1
        
        
            
            
            
        i=0
        for j in range(len(l_prb)):
            if l_prb[i].alive==False:
                del l_prb[i]
                i-=1
            i+=1
        i=0
        for j in range(len(l_prb)):
            l_prb[i].move_and_draw(window)
            if collision1(pygame.Rect(l_prb[i].x,l_prb[i].y,l_prb[i].width,l_prb[i].height),pygame.Rect(p1.x,p1.y,p1.width,p1.height)):
                del l_prb[i]
                p1.power_rb=300
                i-=1
            i+=1
        if boss.health>0:
            boss.general(window)
        
        err=0
        for i in range(len(l_f)):
            if l_f[err].health>0:
                l_f[err].general(window)
                if p1.health!=1:
                    if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                        if p1.health==2:
                            if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                                p1.str="l"
                            elif collision1(pygame.Rect(p1.x+p1.height/2.433962264150943,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                                p1.str="c"
                            else:
                                p1.str="r"
                        
                        p1.health-=1
                        l_f[err].health=0
                else:
                    if p1.str=="l":
                        if collision1(pygame.Rect(p1.x,p1.y,p1.width-p1.height/4.3,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                            p1.health-=1 
                            l_f[err].health=0
                    elif p1.str=="r":
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                            p1.health-=1
                            l_f[err].health=0
                    else:
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_f[err].x,l_f[err].y,l_f[err].width,l_f[err].height)):
                            p1.health-=1
                            l_f[err].health=0
            else:
                del l_f[err]
                err-=1
            err+=1
        if boss.health>=0:
            for i in range(len(l_lr)):
                if collision1(pygame.Rect(boss.x,boss.y,boss.width,boss.height),pygame.Rect(l_lr[i].x,l_lr[i].y,l_lr[i].width,l_lr[i].height)):
                    boss.health-=info["damage"]
                    l_lr[i].health-=1
                    if boss.health<=0:
                        a_r=2
                        for j in range(1,4):
                            for i in range(5):
                                timeSpread = (i*5)*j
                                scaleSpread = HEIGHT/425-(i/10)*2
                                e = Explosion(random.randint(int(boss.x-HEIGHT/30),int(boss.x+boss.width-HEIGHT/90)),random.randint(int(boss.y-HEIGHT/30),int(boss.y+boss.height-HEIGHT/90)),int(HEIGHT/16.6304347826087),int(HEIGHT/16.6304347826087),timeSpread,scaleSpread)
                                l_e.append(e)
                        gm=Green_Mineral(boss.x+boss.width/2,boss.y,HEIGHT/306)
                        break
        if boss.health>=0:
            for i in range(len(l_l)):
                if collision1(pygame.Rect(boss.x,boss.y,boss.width,boss.height),pygame.Rect(l_l[i].x,l_l[i].y,l_l[i].width,l_l[i].height)):
                    boss.health-=info["damage"]
                    l_l[i].health-=1
                    if boss.health<=0:
                        a_r=2
                        for j in range(1,4):
                            for i in range(5):
                                timeSpread = (i*5)*j
                                scaleSpread = HEIGHT/425-(i/10)*2
                                e = Explosion(random.randint(int(boss.x-HEIGHT/30),int(boss.x+boss.width-HEIGHT/90)),random.randint(int(boss.y-HEIGHT/30),int(boss.y+boss.height-HEIGHT/90)),int(HEIGHT/16.6304347826087),int(HEIGHT/16.6304347826087),timeSpread,scaleSpread)
                                l_e.append(e)
                        gm=Green_Mineral(boss.x+boss.width/2,boss.y,HEIGHT/306)
                        break
        if boss.health<1:
            if gm.alive==True:
                if collision1(pygame.Rect(p1.x,p1.y,p1.width,p1.height),pygame.Rect(gm.x,gm.y,gm.width,gm.height)):
                    minerala+=50
                    gm.alive=False
                    whenwin=300
            
        
        
        
            gm.move_and_draw(window)
        if whenwin>0:
            whenwin-=1
            if whenwin==0:
                prozor=0
                l_a,l_l,prozor,l_e,l_m=mainmenu()
            win()
        
        
    pygame.display.update()
    clock.tick(60)
    SVAKIH30+=1
    if SVAKIH30==30:
        SVAKIH30=0
        if time.time()-vremepre>najvecivreme:
            najvecivreme=time.time()-vremepre
        print(time.time()-vremepre)
        vremepre=time.time()