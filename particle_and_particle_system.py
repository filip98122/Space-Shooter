import pygame
import random
pygame.init()
WIDTH,HEIGHT=1540,900
from attractor import *
import math
class Particle:
    def __init__(s,x,y,lifetime,dx,dy,radius,color,alpha,prozor,delay):
        s.x=x
        s.y=y
        s.lifetime=lifetime
        s.dx=dx
        s.dy=dy
        s.distancex=0
        s.distancey=0
        s.distance=0
        s.prozor=prozor
        s.radius=radius
        s.color = color
        s.alpha = alpha
        s.delay=delay
    def draw(s, screen):
        particle_surface = pygame.Surface((s.radius * 2, s.radius * 2), pygame.SRCALPHA) #Create transparent surface.
        pygame.draw.circle(particle_surface, s.color + (s.alpha,), (s.radius, s.radius), s.radius) #draw circle with alpha.
        screen.blit(particle_surface, (int(s.x - s.radius), int(s.y - s.radius))) # blit surface to main screen.
        s.alpha-=0.1
        s.alpha = max(0, s.alpha) # Example of decreasing alpha over time.
class Particle_System:
    """Updates every partcle movment"""
    def __init__(s):
        s.l_p=[]
        s.gravity=0.08
        s.attractor=0
    def draw(s,window,prozor):
        for i in range(len(s.l_p)):
            if s.l_p[i].prozor==prozor:
                if s.l_p[i].delay==0:
                    s.l_p[i].draw(window)
                else:
                    s.l_p[i].delay-=1
    
    
    def update(s,prozor,l_attractors):
        
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
                    if s.l_p[j].prozor==prozor:
                        if s.l_p[j].delay==0:
                            s.l_p[j].distancex=l_attractors[i].x-s.l_p[j].x
                            s.l_p[j].distancey=l_attractors[i].y-s.l_p[j].y
                            s.l_p[j].distance=math.sqrt(s.l_p[j].distancex*s.l_p[j].distancex+s.l_p[j].distancey*s.l_p[j].distancey)
                            s.l_p[j].dx+=(s.l_p[j].distancex*(HEIGHT/1092857.142857143))
                            s.l_p[j].dy+=(s.l_p[j].distancey*(HEIGHT/1092857.142857143))
                #l_attractors[i].draw(window)
                """
                if s.attractor==0:
                    for ii in range(len(l_attractors)):
                        l_attractors[ii].x=random.randint(0,WIDTH)
                        l_attractors[ii].y=random.randint(0,HEIGHT)
                    s.attractor=240
                """
        for i in range(len(s.l_p)):
            if s.l_p[i].lifetime>=1:
                if s.l_p[i].prozor==prozor:
                    if s.l_p[i].delay==0:
                        s.l_p[i].dy+=s.gravity
                        s.l_p[i].x+=s.l_p[i].dx
                        s.l_p[i].y+=s.l_p[i].dy
                        
                        s.l_p[i].lifetime-=1
        #s.attractor-=1
    def spawn(s,maxdx,x,y,liftime,dy,rad,color,alpha,prozor,delay):
        w=random.uniform(0.1,maxdx)
        if_negative=random.randint(1,2)
        if if_negative==1:
            w*=-1
        s.l_p.append(Particle(x,y,liftime,w,dy,rad,color,alpha,prozor,delay))