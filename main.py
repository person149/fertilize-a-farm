import pygame, sys,gif_pygame
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, KEYUP, MOUSEBUTTONDOWN, K_1, K_2, K_3
pygame.init()
#from piskel
timer=pygame.USEREVENT+1
pygame.time.set_timer(timer, 1000)
pi = pygame.image.load("little-man-1.gif")
cherys=gif_pygame.load("cherys guy.gif")
gif_pygame.transform.scale(cherys,(cherys.get_width()*4,cherys.get_height()*4))
grapevine=gif_pygame.load("grape vine (1).gif")
gif_pygame.transform.scale(grapevine,(grapevine.get_width()*4,grapevine.get_height()*4))
chikootree=gif_pygame.load("chikoo (2).gif")
gif_pygame.transform.scale(chikootree,(chikootree.get_width()*4,chikootree.get_height()*4))
ss = False
cherryLocations=[]
grapeLocations=[]
chikooLocations=[]
seletedSeed="grape"
grape=1
cherry=0
chikoo=0
chs = pygame.image.load("chikoo.gif")
chs = pygame.transform.scale(chs,(chs.get_width()*15,chs.get_height()*7))
cs = pygame.image.load("cherry.gif")
cs = pygame.transform.scale(cs,(cs.get_width()*15,cs.get_height()*5))
gs = pygame.image.load("grape.gif")
gs = pygame.transform.scale(gs,(gs.get_width()*15,gs.get_height()*5))
sp = pygame.image.load("New Piskel (3).gif")
sp = pygame.transform.scale(sp,(sp.get_width()*20,sp.get_height()*20))
bt = pygame.image.load("New Piskel (2).gif")
bt = pygame.transform.scale(bt,(bt.get_width()*10,bt.get_height()*10))
WIDTH = 1000
HEIGHT = 800
moneys= 0
basicFont=pygame.font.SysFont(None,40)
fancyFont=pygame.font.SysFont("Comic Sans MS", 20)
running = 7

bt_rect=bt.get_rect(topleft=(0,0))
sp_rect=sp.get_rect(topleft=(200,25))
cs_rect=cs.get_rect(topleft=(260,200))
gs_rect=gs.get_rect(topleft=(260,30))
chs_rect=chs.get_rect(topleft=(260,350))

class Player():
    def __init__(self):
        self.facing = False 
        self.size = 50 +10
        self.speed = 250
        self.move = 0
        self.height = 50
        self.width = 100
        self.x = WIDTH / 2 - self.size / 2
        self.y = HEIGHT - self.height -185


        # self.image = pygame.Surface((self.width, self.height)).convert()
        self.image = pygame.transform.scale(pi,(pi.get_width()*2,pi.get_height()*2))
        # self.image.fill((0, 255, 255))

    def flip(self):
        self.facing = not self.facing
        self.image = pygame.transform.flip(self.image,True,False)
    

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('fertalize a farm')
window.fill((255, 255, 255))

player = Player()  

back = pygame.Surface((WIDTH, HEIGHT))
background = pygame.image.load ("New Piskel.gif")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

while running==7:
    text=basicFont.render(f"{moneys} moneys", True, (0,0,0))
    textRect=text.get_rect()
    textRect.centerx=window.get_rect().centerx+-+-+400
    textRect.centery=window.get_rect().centery-+-+-+300

    tex=fancyFont.render(f"{grape} grape seeds-1", True, (0,0,0))
    textRec=text.get_rect()
    textRec.centerx=window.get_rect().centerx-120
    textRec.centery=window.get_rect().centery-390

    te=fancyFont.render(f"{cherry} cherry seeds-2", True, (0,0,0))
    textRe=text.get_rect()
    textRe.centerx=window.get_rect().centerx-120
    textRe.centery=window.get_rect().centery-370

    t=fancyFont.render(f"{chikoo} chikoo seeds-3", True, (0,0,0))
    textR=text.get_rect()
    textR.centerx=window.get_rect().centerx-120
    textR.centery=window.get_rect().centery-350

    timePassed = clock.tick(30)
    timeSec = timePassed / 1000.0
    player.x += player.move * timeSec

    window.blit(background, (0, 0))
    window.blit(player.image, (player.x, player.y))
    window.blit(text, textRect)
    window.blit(tex, textRec)
    window.blit(te, textRe)
    window.blit(bt,bt_rect)
    window.blit (t,textR)
    for pos in cherryLocations:
        cherys.render(window, pos)
    for pos in grapeLocations:
        grapevine.render(window, pos)
    for pos in chikooLocations:
        chikootree.render(window, pos)
    if ss:  
        window.blit(sp,sp_rect)
        window.blit(cs,cs_rect)
        window.blit(gs,gs_rect)
        window.blit(chs,chs_rect)
    pygame.display.update()
    clock.tick(60)  # limit FPS
    for event in pygame.event.get():
        
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and player.x<954.0:
                if not player.facing:
                    player.flip()   
                player.move = player.speed
            elif event.key == K_LEFT and player.x>-18.0:
                if  player.facing:
                    player.flip()
                player.move = -player.speed
            elif event.key==K_1:
                seletedSeed="grape"
            elif event.key==K_2:
                seletedSeed="cherry"
            elif event.key==K_3:
                seletedSeed="chikoo"
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):  # Fixed condition here too
                player.move = 0
        elif event.type == MOUSEBUTTONDOWN:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if bt_rect.collidepoint(event.pos):
                ss = not ss 
            elif gs_rect.collidepoint(event.pos) and moneys >= 10 and ss:
                moneys -= 10
                grape += 1 
            elif chs_rect.collidepoint(event.pos) and moneys >= 2500 and ss:
                moneys -= 2500
                chikoo += 1 
            elif cs_rect.collidepoint(event.pos) and moneys >= 100 and ss:
                moneys -= 100
                cherry += 1 
            elif mouseY > 625 and cherry>0 and seletedSeed=="cherry":
                cherryLocations.append((mouseX-50, mouseY-126))
                cherry-=1
            elif mouseY > 625 and grape>0 and seletedSeed=="grape":
                grapeLocations.append((mouseX-54, mouseY-126))
                grape-=1
            elif mouseY > 625 and chikoo>0 and seletedSeed=="chikoo":
                chikooLocations.append((mouseX-40, mouseY-125))
                chikoo-=1
        elif event.type==timer:
            moneys+=len(grapeLocations)
            moneys+=len(cherryLocations)*12
            moneys+=len(chikooLocations)*350
    if player.x<=-18.0:
        player.x=-18.0
    if player.x>=954.0:
        player.x=954.0

pygame.quit()
sys.exit()

window.blit(t,textR)


