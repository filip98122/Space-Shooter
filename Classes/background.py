from Classes.loader import *
class Background:
    """Moves and draws the background"""
    def __init__(s,x):
        s.x = x
        s.y = 0
        s.scale = 9
        s.d = random.randint(1,5)
        s.speedy=(HEIGHT/765)*s.d
        if s.d == 5:
            s.image = images[6]
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d <= 3:
            s.image = images[7]
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.d == 4:
            s.image = images[8]
            s.width = s.image.get_width()*(HEIGHT/1000)
            s.height = s.image.get_height()*(HEIGHT/1000)
            s.scaled_img = pygame.transform.scale(s.image, (s.width, s.height))
        if s.speedy==1:
            s.speedy+=1
    def move_and_draw(s,window):
        s.y+=s.speedy
        window.blit(s.scaled_img,(s.x,s.y))