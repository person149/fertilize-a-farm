import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, KEYUP
pygame.init()
#from piskel
pi = pygame.image.load("little-man-1.gif")


WIDTH = 1000
HEIGHT = 800

running = 7

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
pygame.display.set_caption('Python is cool!')
window.fill((255, 255, 255))

player = Player()  

back = pygame.Surface((WIDTH, HEIGHT))
background = pygame.image.load ("New Piskel.gif")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

while running==7:
    timePassed = clock.tick(30)
    timeSec = timePassed / 1000.0
    player.x += player.move * timeSec

    window.blit(background, (0, 0))
    window.blit(player.image, (player.x, player.y))
    pygame.display.update()

    clock.tick(60)  # limit FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if not player.facing:
                    player.flip()   
                player.move = player.speed
            elif event.key == K_LEFT and player.x>=-18.0:
                if  player.facing:
                    player.flip()
                player.move = -player.speed
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):  # Fixed condition here too
                player.move = 0
                print(player.x)
pygame.quit()
sys.exit()





