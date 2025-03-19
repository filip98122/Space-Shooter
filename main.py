#TODO Refactor code. 
# Enable lasers, disable debug lines, make asteroids spawn normal again, up to 60 fps, then refactor.
# File for all classes. Move textures to resources folder. Move save data to saves folder.
# Code should be noticably shorter. Remove classes like rotated laser and handle it correctly.
# Green Mineral and Mineral merge into a single one. Powerups should be one class and have ifs to determine action.
# Combine length is 1800 lines right now. Add some comments to code, for the more complex bits.
# Use normal var names.
# l_l needs to be list_of_lasers, or list_lasers
# Names that should be fixed ( probably some more that I haven't found)
"""
render_death_screen
e2
l_powerup
vremep
kojig
wsmmb #Luka tata mi je to rekao tako da ne bi morao da ponavljam WIDTH/SCALE_MAIN_MENU_BUTTON. Ima jos 3 takva(hsmmb,wssb,hssb)

These are actual variable names...    
"""
from Classes.laser_enemy import *
from Classes.loader import *
from Classes.background import *
from Classes.player import *
from Classes.particle_and_particle_system import *
from Classes.mineral import *
from Classes.green_mineral import *
from Classes.explosion import *
from Classes.asteroid import *
from Classes.fireball import *
from Classes.boss import *
from Classes.button import *
from Classes.laser import *
from Classes.powerup import *
from Classes.functions import *
from Classes.store import *
from Classes.wing_cannos import *
from Classes.drone import *
from Classes.Boss_healthmeter import *
bossh = Boss_healthmeter(WIDTH/2,HEIGHT/22.5)
keydict={
    "shot":keys[pygame.K_SPACE],
    "left":keys[pygame.K_a],
    "right":keys[pygame.K_d],
    "heal":keys[pygame.K_h],
    "up":keys[pygame.K_w],
    "down":keys[pygame.K_s]
}


l_drones=[]
l_background = []
l_wingcannons = []


l_attractors=[Attractor(WIDTH/2,HEIGHT/2,0),
              Attractor(WIDTH/2,HEIGHT/2,0)]
def mainmenu():
    global ukupnom
    global minerala
    global l_powerup
    global whenwin
    global boss
    global l_drones
    l_drones=[]
    for i in range(-5,5):
        l_drones.append(Drone((WIDTH+(WIDTH/2)+(i*(HEIGHT/45)))+(i*(HEIGHT/18))+(HEIGHT/36),(HEIGHT/18)*8,-1))
    boss.health=75
    boss.h25=True
    boss.h50=True
    boss.shoot=100
    global l_f
    global l_le
    l_le=[]
    l_f=[]
    global l_wingcannons
    l_wingcannons=[]
    global p1
    p1.power_db=0
    p1.power_rb=0
    p1.str=""
    l_powerup=[]
    l_a=[]
    l_l=[]
    l_e=[]
    l_m=[]
    p1 = Player(WIDTH/2,HEIGHT,0,0,WIDTH/160)
    ukupnom+=minerala
    minerala=0
    prozor=0
    whenwin=-1
    part.l_p=[]
    return l_a,l_l,prozor,l_e,l_m
l_m = []
l_asteroids = []
l_e = []
start=50
SCALE_MAIN_MENU_BUTTON=273.2142857142857
SCALE_SETTINGS_BUTTON=127.5
wsmmb=WIDTH/SCALE_MAIN_MENU_BUTTON
hsmmb=HEIGHT/SCALE_MAIN_MENU_BUTTON
wssb=WIDTH/SCALE_SETTINGS_BUTTON
hssb=HEIGHT/SCALE_SETTINGS_BUTTON
myfont1 = pygame.font.SysFont('s', int(HEIGHT/12.75))
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

l_powerup=[]
najvecivreme=0
l_s=[
    Store(WIDTH/7.65,HEIGHT/7.65,"fire rate","    Laser exhaust    ",100,7,-1),
    Store(WIDTH/7.65,(HEIGHT/7.65)*2,"damage","    Laser damage    ",100,5,1),
    Store(WIDTH/7.65,(HEIGHT/7.65)*3,"fire rate missle","Wing cannon exhaust",100,120,-2)
]
go_down_int=info["kojidole"]
go_up_int=info["kojig"]
shoot_int=info["kojis"]
go_left_int=info["kojil"]
go_right_int=info["kojid"]
heal_int=info["kojih"]
q=shoot_int
if q==32:
    info["kojis"]=q
    shoot_int=q
    lb[3].text_surface = myfont1.render(f"Change shoot key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojis"]=q
    shoot_int=q
    lb[3].text_surface = myfont1.render(f"Change shoot key from {char[shoot_int-34]}", True, (15, 15, 15))

for i in range(-5,5):
    l_drones.append(Drone((WIDTH+(WIDTH/2)+(i*(HEIGHT/45)))+(i*(HEIGHT/18))+(HEIGHT/36),(HEIGHT/18)*8,-1))
#zakasnije
q=go_up_int
if q==32:
    info["kojig"]=q
    go_up_int=q
    lb[7].text_surface = myfont1.render(f"Change go up key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojig"]=q
    go_up_int=q
    lb[7].text_surface = myfont1.render(f"Change go up key from {char[go_up_int-34]}", True, (15, 15, 15))

q=go_down_int
if q==32:
    info["kojidole"]=q
    go_down_int=q
    lb[8].text_surface = myfont1.render(f"Change go down key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    info["kojidole"]=q
    go_down_int=q
    lb[8].text_surface = myfont1.render(f"Change go down key from {char[go_down_int-34]}", True, (15, 15, 15))


l_f=[]


SVAKIH30=0
myfontwin = pygame.font.SysFont('s', int(HEIGHT/9))
text_surfacewin = myfontwin.render(f"You win!", True, (255,255,255))
widthwin=text_surfacewin.get_width()
heightwin=text_surfacewin.get_height()
def win():
    window.blit(text_surfacewin,(WIDTH/2-widthwin/2,HEIGHT/9))



whenwin=-1

l_le=[]
buttonscrolltimes=1
buttonscrollloc=0
def button_scroll():
    window.blit(imgs,(x,y))
    window.blit(text_surface,(x1,y1))
    #WIDTH/2,HEIGHT/6*5.5

img=pygame.image.load("textures/buttons.png")
text_surface = myfont1.render(f"Next page", True, (0,0,0))
width=lb[3].width
height=lb[3].height
width1=text_surface.get_width()
height1=text_surface.get_height()
imgs=pygame.transform.scale(img,(width,height))
x,y=WIDTH/2-width/2,lb[6].y+lb[6].height
x1,y1=WIDTH/2-width1/2,lb[6].y+lb[6].height+height/2-height1/2
whenwin=0
l_wingcannons=[]
q=go_left_int
if q==32:
    go_left_int=q
    info["kojil"]=q
    lb[4].text_surface = myfont1.render(f"Change go left key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    go_left_int=q
    info["kojil"]=q
    lb[4].text_surface = myfont1.render(f"Change go left key from {char[go_left_int-34]}", True, (15, 15, 15))
q=go_right_int
if q==32:
    go_right_int=q
    info["kojid"]=q
    lb[5].text_surface = myfont1.render(f"Change go right key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    go_right_int=q
    info["kojid"]=q
    lb[5].text_surface = myfont1.render(f"Change go right key from {char[go_right_int-34]}", True, (15, 15, 15))
button_scrollhold=False
q=heal_int
if q==32:
    heal_int=q
    info["kojih"]=q
    lb[6].text_surface = myfont1.render(f"Change heal key from Space", True, (15, 15, 15))
if q>=33 and q<=126:
    heal_int=q
    info["kojih"]=q
    lb[6].text_surface = myfont1.render(f"Change heal key from {char[heal_int-34]}", True, (15, 15, 15))
prom(3,lb)
prom(4,lb)
prom(5,lb)
prom(6,lb)
prom(7,lb)
prom(8,lb)
godmode=False
boss.shoot=100
spawn_background_rate=int(14780/WIDTH)
render_death_screen=1
ukupnom=info["minerala"]
minerala = 0
prozor=0
washolding=False
vremepre=time.time()
while True:
    if prozor==-1:
        if render_death_screen==1:
            render_death_screen=0
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
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
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
                render_death_screen=1
                l_asteroids,l_l,prozor,l_e,l_m=mainmenu()
        if keys[pygame.K_ESCAPE]:
            if washolding==False:
                prozor=0
                render_death_screen=1
                l_asteroids,l_l,prozor,l_e,l_m=mainmenu()
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
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        window.fill("Black")
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
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
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        window.fill("Black")
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
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
        #GO UP CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
        #GO UP CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
        #GO UP CODE IS BELOW |||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[7].width,lb[7].height,lb[7].x,lb[7].y,mousePos,mouseState):
            q = checker(keys,go_up_int)
            if q==32:
                info["kojig"]=q
                go_up_int=q
                lb[7].text_surface = myfont1.render(f"Change go up key from Space", True, (15, 15, 15))
                prom(7,lb)
            if q>=33 and q<=126:
                info["kojig"]=q
                go_up_int=q
                lb[7].text_surface = myfont1.render(f"Change go up key from {char[go_up_int-34]}", True, (15, 15, 15))
                prom(7,lb)
        #GO DOWN CODE IS BELOW |||||||||||||||||||||||||||||||||||||
        #GO DOWN CODE IS BELOW |||||||||||||||||||||||||||||||||||||
        #GO DOWN CODE IS BELOW |||||||||||||||||||||||||||||||||||||
        if button_colision(lb[8].width,lb[8].height,lb[8].x,lb[8].y,mousePos,mouseState):
            q = checker(keys,go_down_int)
            if q==32:
                info["kojidole"]=q
                go_down_int=q
                lb[8].text_surface = myfont1.render(f"Change go down key from Space", True, (15, 15, 15))
                prom(8,lb)
            if q>=33 and q<=126:
                info["kojidole"]=q
                go_down_int=q
                lb[8].text_surface = myfont1.render(f"Change go down key from {char[go_down_int-34]}", True, (15, 15, 15))
                prom(8,lb)
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
#SETTINGS CODE IS BELOW ||||||||||||||||||||||||||||||||||||||||||||
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
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        window.fill("Black")
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
            
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
            q = checker(keys,shoot_int)
            if q==32:
                info["kojis"]=q
                shoot_int=q
                lb[3].text_surface = myfont1.render(f"Change shoot key from Space", True, (15, 15, 15))
                prom(3,lb)
            if q>=33 and q<=126:
                info["kojis"]=q
                shoot_int=q
                lb[3].text_surface = myfont1.render(f"Change shoot key from {char[shoot_int-34]}", True, (15, 15, 15))
                prom(3,lb)
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
    #GOING LEFT CODE BELOW |||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[4].width,lb[4].height,lb[4].x,lb[4].y,mousePos,mouseState):
            q = checker(keys,go_left_int)
            if q==32:
                go_left_int=q
                info["kojil"]=q
                lb[4].text_surface = myfont1.render(f"Change go left key from Space", True, (15, 15, 15))
                prom(4,lb)
            if q>=33 and q<=126:
                go_left_int=q
                info["kojil"]=q
                lb[4].text_surface = myfont1.render(f"Change go left key from {char[go_left_int-34]}", True, (15, 15, 15))
                prom(4,lb)
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
    #GOING RIGHT CODE BELOW ||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[5].width,lb[5].height,lb[5].x,lb[5].y,mousePos,mouseState):
            q = checker(keys,go_right_int)
            if q==32:
                go_right_int=q
                info["kojid"]=q
                lb[5].text_surface = myfont1.render(f"Change go right key from Space", True, (15, 15, 15))
                prom(5,lb)
            if q>=33 and q<=126:
                go_right_int=q
                info["kojid"]=q
                lb[5].text_surface = myfont1.render(f"Change go right key from {char[go_right_int-34]}", True, (15, 15, 15))
                prom(5,lb)
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
    #HEALING CODE BELOW ||||||||||||||||||||||||||||||||||||||||||||
        if button_colision(lb[6].width,lb[6].height,lb[6].x,lb[6].y,mousePos,mouseState):
            q = checker(keys,heal_int)
            if q==32:
                heal_int=q
                info["kojih"]=q
                lb[6].text_surface = myfont1.render(f"Change heal key from Space", True, (15, 15, 15))
                prom(6,lb)
            if q>=33 and q<=126:
                heal_int=q
                info["kojih"]=q
                lb[6].text_surface = myfont1.render(f"Change heal key from {char[heal_int-34]}", True, (15, 15, 15))
                prom(6,lb)   
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
                try:
                    print(30/najvecivreme)
                except:
                    exit()
                exit()
        if keys[pygame.K_ESCAPE]:
            if washolding==False:
                write(info)
                ens(info)
                print(najvecivreme)
                try:
                    print(30/najvecivreme)
                except:
                    exit()
                exit()
        else:
            washolding=False
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        window.fill("Black")
        # Spawn new particles if needed
        if random.randint(1,int(HEIGHT/300))==1:
            part.spawn(3,WIDTH/2+WIDTH/2.566666666666667,HEIGHT/2-WIDTH/5.133333333333333,250,-10,HEIGHT/(16.6304347826087*5),(random.randint(118, 138), random.randint(0, 20), random.randint(118, 138)),random.randint(70, 150),0,0)
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
        for i in range(len(lb)):
            if lb[i].prozor==0:
                lb[i].draw(window)
        if button_colision(lb[0].width,lb[0].height,lb[0].x,lb[0].y,mousePos,mouseState):prozor=1
        if button_colision(lb[1].width,lb[1].height,lb[1].x,lb[1].y,mousePos,mouseState):prozor=3
        if button_colision(lb[2].width,lb[2].height,lb[2].x,lb[2].y,mousePos,mouseState):prozor=2
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    #GAME CODE IS BELOW |||||||||||||||||||||||||||||||||||||||||||||||
    if prozor==1:
        if not godmode==False:
            p1.health=3
        if info["fire rate"]<7:
            info["fire rate"]=7
        keys = pygame.key.get_pressed()
        levo =keys[go_left_int]
        desno=keys[go_right_int]
        pucaj=keys[shoot_int]
        heluj=keys[heal_int]
        gore=keys[go_up_int]
        dole=keys[go_down_int]
        keydict["left"]=levo
        keydict["right"]=desno
        keydict["shot"]=pucaj
        keydict["heal"]=heluj
        keydict["up"]=gore
        keydict["down"]=dole
        if boss.health>0:
            a_r = random.randint(1,int((14800)/WIDTH))
        if a_r == 1:
            ast = Asteroid(random.randint(0,WIDTH-int(HEIGHT/16.6304347826087)),-int((HEIGHT/16.6304347826087)+10),info['asteroid health'])
            l_asteroids.append(ast)
        e = random.randint(1,spawn_background_rate)
        if e == 1:
            e = random.randint(0,int(WIDTH-(28*(HEIGHT/1000))))
            l_background.append(Background(e))
        window.fill("Black")
        for i in range(len(l_background)):
            l_background[i].move_and_draw(window)
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                if info["highscore"]<minerala:
                    info["highscore"]=minerala
                l_asteroids,l_l,prozor,l_e,l_m=mainmenu()
        if keys[pygame.K_ESCAPE]:
            prozor=0
            if info["highscore"]<minerala:
                info["highscore"]=minerala
            l_asteroids,l_l,prozor,l_e,l_m=mainmenu()
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
        indexdelete = 0
        if boss.health>0 or len(l_asteroids)>0 or len(l_le)>0:
             if keydict["shot"]:
                if p1.time_missle<=0:
                    l_wingcannons.append(Wing_cannons(p1.x,p1.y))
                    l_wingcannons.append(Wing_cannons(p1.x+p1.width,p1.y))
                    p1.time_missle=info["fire rate missle"]
                if p1.time <= 0:
                    l1 = Laser(p1.x+p1.width/2,info["damage"],0,p1,0,p1.y)
                    if p1.power_db>0:
                        l2=Laser(p1.x+p1.width/2,info["damage"],0,p1,1,p1.y)
                        l_l.append(l2)
                    p1.time = info["fire rate"]
                    l_l.append(l1)
                    if p1.power_rb>0:
                        if p1.power_db==0:
                            if p1.str=="r" or p1.str=="" or p1.str=="c":
                                l1r=Laser(p1.x-p1.width/12.9,info["damage"],45,p1,0,p1.y-(p1.height/11.9)*2)
                                l_l.append(l1r)
                            if p1.str=="l" or p1.str=="" or p1.str=="c":
                                l1r=Laser(p1.x+(p1.width/12.9)*9,info["damage"],315,p1,0,p1.y-(p1.height/11.9)*2)
                                l_l.append(l1r)
                        else:
                            if p1.str=="r" or p1.str=="" or p1.str=="c":
                                l1r=Laser(p1.x-p1.width/12.9,info["damage"],45,p1,0,(p1.y-(p1.height/11.9)*2))
                                l_l.append(l1r)
                                l1r=Laser(p1.x-p1.width/12.9,info["damage"],45,p1,1,(p1.y-(p1.height/11.9)*2))
                                l_l.append(l1r)
                            if p1.str=="l" or p1.str=="" or p1.str=="c":
                                l1r=Laser(p1.x+(p1.width/12.9)*9,info["damage"],315,p1,0,(p1.y-(p1.height/11.9)*2))
                                l_l.append(l1r)
                                l1r=Laser(p1.x+(p1.width/12.9)*9,info["damage"],315,p1,1,(p1.y-(p1.height/11.9)*2))
                                l_l.append(l1r)
        for i in range(len(l_l)):
            if l_l[i].health != 0:
                l_l[i].draw(window)
        #background
        if keydict["heal"]:
            if p1.health<=2:
                if minerala>=35:
                    p1.health+=1
                    minerala-=35
                    if p1.health==2:
                        p1.str=""
        indexdelete=0
        for i in range(len(l_background)):
            if l_background[indexdelete].y >= HEIGHT:
                del l_background[indexdelete]
                indexdelete-=1
            indexdelete+=1
        #asteroids
        for i in range(len(l_asteroids)):
            if l_asteroids[i].strana==0:
                l_asteroids[i].draw(window)
        indexdelete = 0
        for i in range(len(l_asteroids)):
            if l_asteroids[indexdelete].y >= HEIGHT:
                del l_asteroids[indexdelete]
                indexdelete-=1
            indexdelete+=1
            
        err = 0
        for i in range(len(l_asteroids)):
            if l_asteroids[err].x>=p1.x-l_asteroids[err].width and l_asteroids[err].x<=p1.x+p1.width and l_asteroids[err].y>=p1.y-l_asteroids[err].height and l_asteroids[err].y<=p1.y+p1.height:
                if p1.health!=1:
                    if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                        if p1.health==2:
                            if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                                p1.str="l"
                            elif collision1(pygame.Rect(p1.x+p1.height/2.433962264150943,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                                p1.str="c"
                            else:
                                p1.str="r"
                        if not godmode:
                            p1.health-=1
                        l_asteroids[err].alive=0
                        l_asteroids[err].drop=False
                else:
                    if p1.str=="l":
                        if collision1(pygame.Rect(p1.x,p1.y,p1.width-p1.height/4.3,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                            if not godmode:
                                p1.health-=1 
                            l_asteroids[err].alive=0
                            l_asteroids[err].drop=False
                    elif p1.str=="r":
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                            if not godmode:
                                p1.health-=1
                            l_asteroids[err].alive=0
                            l_asteroids[err].drop=False
                    else:
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_asteroids[err].x,l_asteroids[err].y,l_asteroids[err].width,l_asteroids[err].height)):
                            if not godmode:
                                p1.health-=1
                            l_asteroids[err].alive=0
                            l_asteroids[err].drop=False
            err +=1
        for i in range(len(l_l)):
            for j in range(len(l_asteroids)):
                
                if collision1(pygame.Rect(l_l[i].x,l_l[i].y,l_l[i].width,l_l[i].height),pygame.Rect(l_asteroids[j].x,l_asteroids[j].y,l_asteroids[j].width,l_asteroids[j].height)):         
                    if l_asteroids[j].alive >= 0:
                        l_l[i].health-=1
                        for ii in range(10):
                            part.spawn(2,l_l[i].x+l_l[i].width/2,l_l[i].y+l_l[i].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(17, 77),random.randint(205, 255),random.randint(186,246)),random.randint(70, 150),1,random.randint(0,40))
                        l_asteroids[j].alive-=info['damage']




        for i in range(len(l_drones)):
            l_drones[i].general(window)
            if l_drones[i].shoot==0:
                l_le.append(Laser_enemy(l_drones[i].x+l_drones[i].width/2,l_drones[i].y+l_drones[i].height))
                l_drones[i].shoot=random.randint(180,240)
        err=0
        for i in range(len(l_le)):
            l_le[err].general(window)
            if l_le[err].x>=p1.x-l_le[err].width and l_le[err].x<=p1.x+p1.width and l_le[err].y>=p1.y-l_le[err].height and l_le[err].y<=p1.y+p1.height:
                if p1.health!=1:
                    if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                        if p1.health==2:
                            if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                                p1.str="l"
                            elif collision1(pygame.Rect(p1.x+p1.height/2.433962264150943,p1.y,p1.height/5.608695652173913,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                                p1.str="c"
                            else:
                                p1.str="r"
                        if not godmode:
                            p1.health-=1
                        l_le[err].alive=0
                else:
                    if p1.str=="l":
                        if collision1(pygame.Rect(p1.x,p1.y,p1.width-p1.height/4.3,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                            if not godmode:
                                p1.health-=1 
                            l_le[err].alive=0
                    elif p1.str=="r":
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                            if not godmode:
                                p1.health-=1
                            l_le[err].alive=0
                    else:
                        if collision1(pygame.Rect(p1.x+p1.height/4.3,p1.y,p1.width-p1.height/2.15,p1.height),pygame.Rect(l_le[err].x,l_le[err].y,l_le[err].width,l_le[err].height)):
                            if not godmode:
                                p1.health-=1
                            l_le[err].alive=0
           
            if l_le[err].alive==False:
                del l_le[err]
                err-=1
            err+=1
        for i in range(len(l_drones)):
            for j in range(len(l_l)):
                if collision1(pygame.Rect(l_drones[i].x,l_drones[i].y,l_drones[i].width,l_drones[i].height),pygame.Rect(l_l[j].x,l_l[j].y,l_l[j].width,l_l[j].height)):
                    if l_drones[i].health>0 and l_l[j].health>0:
                        l_drones[i].health-=info['damage']
                        l_l[j].health=0
                        for ii in range(10):
                            part.spawn(2,l_l[j].x+l_l[j].width/2,l_l[j].y+l_l[j].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(17, 77),random.randint(205, 255),random.randint(186,246)),random.randint(70, 150),1,random.randint(0,40))
        for i in range(len(l_wingcannons)):
            for j in range(len(l_drones)):
                if collision1(pygame.Rect(l_wingcannons[i].x,l_wingcannons[i].y,l_wingcannons[i].width,l_wingcannons[i].height),pygame.Rect(l_drones[j].x,l_drones[j].y,l_drones[j].width,l_drones[j].height)):
                    if l_drones[i].health>0:
                        l_drones[j].health-=3
                        for ii in range(10):
                            part.spawn(2,l_drones[j].x+l_drones[j].width/2,l_drones[j].y+l_drones[j].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(113, 173),random.randint(100, 160),random.randint(3,63)),random.randint(70, 150),1,random.randint(0,40))
                        l_wingcannons[i].alive=False
        indexdelete=0
        for i in range(len(l_drones)):
            if l_drones[indexdelete].health<=0:
                for j in range(5):
                    timeSpread = (j*5)
                    scaleSpread = HEIGHT/425-(j/10)*2
                    e = Explosion(random.randint(int(l_drones[i].x-HEIGHT/30),int(l_drones[i].x+l_drones[i].width)),random.randint(int(boss.y-HEIGHT/30),int(boss.y+boss.height-HEIGHT/90)),int(HEIGHT/16.6304347826087),int(HEIGHT/16.6304347826087),timeSpread,scaleSpread)
                    l_e.append(e)
                del l_drones[indexdelete]
                indexdelete-=1
            indexdelete+=1
        for i in range(len(l_wingcannons)):
            for j in range(len(l_asteroids)):
                if collision1(pygame.Rect(l_wingcannons[i].x,l_wingcannons[i].y,l_wingcannons[i].width,l_wingcannons[i].height),pygame.Rect(l_asteroids[j].x,l_asteroids[j].y,l_asteroids[j].width,l_asteroids[j].height)):
                    l_asteroids[j].alive=0
                    for ii in range(10):
                        part.spawn(2,l_asteroids[j].x+l_asteroids[j].width/2,l_asteroids[j].y+l_asteroids[j].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(113, 173),random.randint(100, 160),random.randint(3,63)),random.randint(70, 150),1,random.randint(0,40))
        if boss.health>0:
            for i in range(len(l_wingcannons)):
                if collision1(pygame.Rect(l_wingcannons[i].x,l_wingcannons[i].y,l_wingcannons[i].width,l_wingcannons[i].height),pygame.Rect(boss.x,boss.y,boss.width,boss.height)):
                    l_wingcannons[i].alive=False
                    boss.health-=3
                    for ii in range(10):
                        part.spawn(2,l_wingcannons[i].x+l_wingcannons[i].width/2,l_wingcannons[i].y+l_wingcannons[i].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(113, 173),random.randint(100, 160),random.randint(3,63)),random.randint(70, 150),1,random.randint(0,40))
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
        err=0
        for i in range(len(l_wingcannons)):
            if l_wingcannons[err].alive==True:
                l_wingcannons[err].general(window)
            else:
                del l_wingcannons[err]
                err-=1
            err+=1
        err = 0
        for i in range(len(l_asteroids)):
            if l_asteroids[err].alive <= 0:
                if l_asteroids[err].drop==True:
                    prob_powerup= random.randint(1,15)
                    if prob_powerup==1:
                        p=Power_up(l_asteroids[err].x,l_asteroids[err].y,"rb")
                        l_powerup.append(p)
                    elif prob_powerup==2:
                        p=Power_up(l_asteroids[err].x,l_asteroids[err].y,"db")
                        l_powerup.append(p)
                    else:
                        m = Mineral(l_asteroids[err].x,l_asteroids[err].y,HEIGHT/306)
                        l_m.append(m)
                for i in range(5):
                    timeSpread = i*5
                    scaleSpread = HEIGHT/425-(i/10)*2
                    e = Explosion(random.randint(int(l_asteroids[err].x-HEIGHT/30),int(l_asteroids[err].x+l_asteroids[err].width-HEIGHT/90)),random.randint(int(l_asteroids[err].y-HEIGHT/30),int(l_asteroids[err].y+l_asteroids[err].height-HEIGHT/90)),l_asteroids[err].width,l_asteroids[err].height,timeSpread,scaleSpread)
                    l_e.append(e)
                del l_asteroids[err]
                err-=1
            err+=1
        if boss.health>0:
            boss.general(window,l_f,p1)
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
                for ii in range(10):
                    part.spawn(2,l_m[i].x+l_m[i].width/2,l_m[i].y+l_m[i].height/2,random.randint(20,120),-1,HEIGHT/180,(random.randint(140, 200),0,0),random.randint(70, 150),1,random.randint(0,40))
                
        err = 0
        for i in range(len(l_m)):
            if l_m[err].alive == False:
                del l_m[err]
                err-=1
            err+=1
            
        p1.draw(window)
        p1.move(keydict)
        #asteroids
        for i in range(len(l_asteroids)):
            if l_asteroids[i].strana==1:
                l_asteroids[i].draw(window)
        indexdelete = 0
        for i in range(len(l_asteroids)):
            if l_asteroids[indexdelete].y >= HEIGHT:
                del l_asteroids[indexdelete]
                indexdelete-=1
            indexdelete+=1
        
        
        
        i=0
        for j in range(len(l_powerup)):
            l_powerup[i].move_and_draw(window)
            if collision1(pygame.Rect(l_powerup[i].x,l_powerup[i].y,l_powerup[i].width,l_powerup[i].height),pygame.Rect(p1.x,p1.y,p1.width,p1.height)):
                if l_powerup[i].link=="db":
                    p1.power_db=300
                else:
                    p1.power_rb=300
                i-=1
                del l_powerup[i+1]
            i+=1
        
        
            
            
            
            
        
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
        if boss.health>=1:
            for i in range(len(l_l)):
                if collision1(pygame.Rect(boss.x,boss.y,boss.width,boss.height),pygame.Rect(l_l[i].x,l_l[i].y,l_l[i].width,l_l[i].height)):
                    boss.health-=info["damage"]
                    for ii in range(10):
                        part.spawn(2,l_l[i].x+l_l[i].width/2,l_l[i].y+l_l[i].height/2,random.randint(10,60),-1,HEIGHT/180,(random.randint(17, 77),random.randint(205, 255),random.randint(186,246)),random.randint(70, 150),1,random.randint(0,40))
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
                if gm.y >= HEIGHT:
                    gm.alive = False
                    whenwin=300
            
        
        
        
            gm.move_and_draw(window)
        if whenwin>0:
            whenwin-=1
            if whenwin==0:
                prozor=0
                l_asteroids,l_l,prozor,l_e,l_m=mainmenu()
            win()
        if boss.health<=50 and boss.h50:
            for i in range(2):
                for i in range(-5,5):
                    l_drones.append(Drone((WIDTH+(WIDTH/2)+(i*(HEIGHT/45)))+(i*(HEIGHT/18))+(HEIGHT/36),(HEIGHT/18)*7,-1))
                timeSpread = i*5
                scaleSpread = HEIGHT/425-(i/10)*2
                e = Explosion(random.randint(int(boss.x-HEIGHT/30),int(boss.x+boss.width-HEIGHT/90)),random.randint(int(boss.y-HEIGHT/30),int(boss.y+boss.height-HEIGHT/90)),int(HEIGHT/16.6304347826087),int(HEIGHT/16.6304347826087),timeSpread,scaleSpread)
                l_e.append(e)
            boss.h50=False
        if boss.health<=25 and boss.h25:
            for i in range(-5,5):
                l_drones.append(Drone((WIDTH+(WIDTH/2)+(i*(HEIGHT/45)))+(i*(HEIGHT/18))+(HEIGHT/36),(HEIGHT/18)*6,-1))
            for i in range(3):
                timeSpread = i*5
                scaleSpread = HEIGHT/425-(i/10)*2
                e = Explosion(random.randint(int(boss.x-HEIGHT/30),int(boss.x+boss.width-HEIGHT/90)),random.randint(int(boss.y-HEIGHT/30),int(boss.y+boss.height-HEIGHT/90)),int(HEIGHT/16.6304347826087),int(HEIGHT/16.6304347826087),timeSpread,scaleSpread)
                l_e.append(e)
            boss.h25=False
        if boss.health>0:
            bossh.draw(window,boss.health)
    part.draw(window,prozor)
    part.update(prozor,l_attractors)

    pygame.display.update()
    clock.tick(60)
    SVAKIH30+=1
    if SVAKIH30==30:
        SVAKIH30=0
        if time.time()-vremepre>najvecivreme:
            najvecivreme=time.time()-vremepre
        print(time.time()-vremepre)
        vremepre=time.time()