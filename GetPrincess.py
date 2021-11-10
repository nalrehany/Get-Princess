import pygame
import math

# Initialize the pygame
pygame.init()

# Setting up the screen and background
screen = pygame.display.set_mode((1000,900))

# Background
background_image = pygame.image.load('background.jpg').convert()

# Title and Icon of window
pygame.display.set_caption("Get Princess")

# Icon on top of window
icon = pygame.image.load('knight.png')
pygame.display.set_icon(icon)

# Setting some colours to be used for the pop-up text
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
font = pygame.font.Font('freesansbold.ttf', 44)
text = font.render('WELL DONE, The Princess is yours', True, white)
textRect = text.get_rect()  

winningknightimg = pygame.image.load('knightwin.png')
winningknightimg = pygame.transform.scale(winningknightimg, (300, 300))

winningheartimg = pygame.image.load('like.png')
winningheartimg = pygame.transform.scale(winningheartimg, (200, 200))

winningprincessimg = pygame.image.load('princesswin.png')
winningprincessimg = pygame.transform.scale(winningprincessimg, (300, 300))

explosion = pygame.image.load('explosion.png')
explosion = pygame.transform.scale(explosion, (60, 60))


#Princess Image
princessImg = pygame.image.load('princess.png')
princessImg = pygame.transform.scale(princessImg, (50,50))
princessX = 500
princessY = 20
princessX_change = 0
princessY_change = 0

# Player/knight class
class player():
    def __init__(self, playerX, playerY, playerX_change, playerY_change):
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.playerY_change = playerY_change
        self.playerImg = pygame.image.load('knight.png')
        self.playerImg = pygame.transform.scale(self.playerImg, (50,50))
        self.rect = pygame.Rect(32,32,16,16)
        
# Drawing the knight on the screen 
    def pdraw(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
            
# Movement mechanics of the player using arrow keys
    def pmovement(self):
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.playerY_change = -0.8
            if event.key == pygame.K_DOWN:
                self.playerY_change = 0.8
            if event.key == pygame.K_LEFT:
                self.playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.playerY_change = 0

# Creating boundaries so player can not go outside of window
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 950:
            self.playerX = 950
        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 850:
            self.playerY = 850

# Goblin class
class goblin():
    def __init__(self, goblinX, goblinY, goblinX_change, goblinY_change):
        self.goblinX = goblinX
        self.goblinY = goblinY
        self.goblinX_change = goblinX_change
        self.goblinY_change = goblinY_change
        self.goblinImg = pygame.image.load('goblin.png')
        self.goblinImg = pygame.transform.scale(self.goblinImg,(40,40))
 
# Drawing the goblins on the screen    
    def draw(self):
        screen.blit(self.goblinImg, (self.goblinX, self.goblinY))
        
# Movement mechanics of the goblins across the screen  
    def movement(self):
        self.goblinX += self.goblinX_change
        if self.goblinX <= 0 or self.goblinX >= 950:
            self.goblinX_change = self.goblinX_change * -1
        self.goblinY += self.goblinY_change
        if self.goblinY <= 0 or self.goblinY >= 850:
            self.goblinY_change = self.goblinY_change * -1


# Princess class and drawing
def princess(x,y):
    screen.blit(princessImg, (x, y))

# Instantiating objects of player and goblin classes
p = player(500, 520, 0, 0) 
g = goblin(160, 80, 4, 0)
g1 = goblin(60, 200, 0.8, 0)
g2 = goblin(360, 280, 1.9, 0)
g3 = goblin(360, 340, 2, 0)
g4 = goblin(360, 400, 2.5, 0)
g5 = goblin(950, 300, 0, 1.8)
g6 = goblin(0, 300, 0, 1.8)
g7 = goblin(0, 650, 2.2, 0)
g8 = goblin(0, 750, 1.8, 0)
g9 = goblin(0, 450, 2.1, 0)

# Making a list for easy looping in methods
goblinlist = [g, g1, g2, g3, g4, g5, g6, g7, g8, g9] # Made for easy access in method calling

# Collision detection
def isCollision(playerX, playerY, goblinX, goblinY):
    global p
    dx = playerX - goblinX
    dy = playerY - goblinY
    distance = math.sqrt(math.pow(dx,2) + math.pow(dy,2)) # Distance formula for 2 points
    if distance < 40:
        pygame.display.update()
        p = player(500, 520, 0,0) # Send the knight back to starting point

# Collision detection between player and objectivr
def winningcollision(playerX, playerY, princessX, princessY):
    global p
    disx = playerX - princessX
    disy = playerY - princessY
    distance = math.sqrt(math.pow(disx,2) + math.pow(disy,2)) # Distance formula for 2 points
    if distance < 40:
        #screen.blit(text, textRect)
        #textRect.center = (500,300) # Winning text displayed when reached objective
        screen.blit(winningknightimg, (150, 300))
        screen.blit(winningprincessimg, (550, 300))
        screen.blit(winningheartimg, (400, 300))


explosionList = []

# Window and game functionality       
running = True
while running:

    #RGB
    screen.fill((0,0,0))
   
    # Background Image
    screen.blit(background_image, (0,0))

    current_time = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                     
    princess(princessX, princessY)
    
# Calling class methods for all goblins in a loop
    for gob in goblinlist:
        gob.movement()
        gob.draw()
  

# Calling player class method    
    p.pmovement()
    p.pdraw()

# Collision detection loop for goblins
    for gob in goblinlist:
        isCollision(p.playerX, p.playerY, gob.goblinX, gob.goblinY)
       


# Collision detection for player and objective
    winningcollision(p.playerX, p.playerY, princessX, princessY)
    
# Continuously update the screen
    pygame.display.update()
