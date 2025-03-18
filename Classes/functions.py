from General_info import *
from Classes.particle_and_particle_system import *
from Classes.player import *
from Classes.boss import *

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


WIDTH,HEIGHT=1540,900
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def collision1(rect1 : pygame.Rect,rect2 : pygame.Rect):
    if rect1.colliderect(rect2):
        return True
    return False

char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def change(index1,index2,index1c,index2c):
    info[index1]+=index1c
    info[index2]+=index2c
def read():
    info=end()
    return info

info=read()
ukupnom=info['minerala']
minerala=0
def write(info):
    info["minerala"]=ukupnom
    info["minerala"]=0
    info={'minerala': 0, 'username': '', 'kojis': 32, 'kojil': 97, 'kojid': 100, 'kojih': 104, 'fire rate': 13, 'highscore': 546, 'damage': 1, 'fire rate missle': 180, 'kojidole': 115, 'kojig': 119, 'asteroid health': 1,}
    ens(info)
go_down_int=info["kojidole"]
go_up_int=info["kojig"]
shoot_int=info["kojis"]
go_left_int=info["kojil"]
go_right_int=info["kojid"]
heal_int=info["kojih"]


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


    
    
    
    
    
    
    



def checker(keys,index):
    pressed = 0
    for key in range(512):
        if key==106:
            #breakpoint()
            pass
        if keys[key]:
            pressed = key
            break
        
    if pressed!=0 and pressed!=heal_int and pressed!=shoot_int and pressed!=go_right_int and pressed!=go_left_int and pressed!=go_up_int and pressed!=go_down_int:
        return pressed
    else:
        return index


def Vector_Normalization(x1, y1, x2, y2):
    # Calculate dx and dy with direction
    distancex = x2 - x1
    distancey = y2 - y1
    vector_lenght=math.sqrt(distancex*distancex+distancey*distancey)
    distancex=distancex/vector_lenght
    distancey=distancey/vector_lenght
    distancex*=HEIGHT/150 # For speed
    distancey*=HEIGHT/150 # For speed
    return distancex,distancey
def get_angle(dx,dy):
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)
    return angle_deg
def draw_minerals(x,y,window,minerala):
    img = pygame.image.load("textures/mineral.png")
    width = HEIGHT/25.5
    height = HEIGHT/25.5
    scaled_img = pygame.transform.scale(img, (width, height))
    window.blit(scaled_img,(x,y))
    myfont = pygame.font.SysFont('B', int(HEIGHT/17))
    text_surface = myfont.render(f"{minerala}", True, (255, 255, 255))
    window.blit(text_surface,(x+width+WIDTH/76.5,y))
def prom(index,lb):
    lb[index].width1=lb[index].text_surface.get_width()
    lb[index].height1=lb[index].text_surface.get_height()