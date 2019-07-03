import os
import random
import pygame
import time

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(30,30,60,60)

    def move(self,dx,dy):
        if dx!=0:
            self.move_single_axis(dx,0)
        if dy!=0:
            self.move_single_axis(0,dy)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

#a new class for walls / blocks to jump onto        
class Wall(object):
    def __init__(self, wx, wy):
        walls.append(self)
        self.rect = pygame.Rect(wx,wy,30,30)

    def reset_wall(self):
        self.active = False

#subroutines for main program

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text, top, left,size):
    #set font & size
    my_text = pygame.font.Font('freesansbold.ttf',size)
    #create text objects
    text_surface, text_rect = text_objects(text, my_text)
    #set where the text appears on screen
    text_rect.center = ((top),(left))
    screen.blit(text_surface, text_rect)

    
def load_high_score():
    high_score = 0
    
    try:
        save_file = open("save.txt", "r")
        high_score = int(save_file.read())
        save_file.close()
    except IOError:
        print("No high score available.")
    except ValueError:
        print("File error. High score set to zero.")
 
    return high_score
 
 
def save_high_score(high_score):
    try:
        save_file = open("save.txt", "w")
        save_file.write(str(high_score))
        save_file.close()
    except IOError:
        print("Unable to save.")




#start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.font.init()


#set up display
pygame.display.set_caption("Jump to escape!")
width = 620
height = 540
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

walls = []
player = Player() #create a player object using the class above
colour = (0,128,255)
wall_colour = (255,255,255)
current_score = 0

#In the level, W means wall & E means exit


level = [
"WWWWWWWWWWWWWWWWWWWWW",
"W                   W",
"W                   W",
"W                   W",
"W                E  W",
"W           WWWWWW  W",
"W                   W",
"W                   W",
"W  WWWWW            W",
"W                   W",
"W                WWWW",
"W                   W",
"W                   W",
"W      WWWWWW       W",
"W                   W",
"W                   W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
]

levels = [[
"WWWWWWWWWWWWWWWWWWWWW",
"W                   W",
"W                   W",
"W                   W",
"W                E  W",
"W           WWWWWW  W",
"W                   W",
"W                   W",
"W  WWWWW            W",
"W                   W",
"W                WWWW",
"W                   W",
"W                   W",
"W      WWWWWW       W",
"W                   W",
"W                   W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
],[
"WWWWWWWWWWWWWWWWWWWWW",
"W                   W",
"W E                 W",
"W WWWWW             W",
"W     WWW           W",
"W                   W",
"W                   W",
"W         WWWWW     W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"W      WWWWWW       W",
"W                   W",
"W                   W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
],[
"WWWWWWWWWWWWWWWWWWWWW",
"W                   W",
"W             W     W",
"W        WWW  W    WW",
"W             W E WWW",
"W  WWWW             W",
"W                   W",
"W         WWWWW     W",
"W                   W",
"W                   W",
"W    W              W",
"W                   W",
"W                   W",
"W         WWW       W",
"W                   W",
"W   W               W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
]]
          

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall(x, y)
        if col == "E":
            end_rect = pygame.Rect(x,y,30,30)
        x += 30
    y += 30
    x=0



#start the game play!
running = True

pygame.mixer.music.load("background_music.mp3")

pygame.mixer.music.play(-1) # the -1 is the loops, so here is infinite 

screen.fill((0,0,0))
message_display("Use arrows & space bar to get to the exit!",300,300,20)
pygame.display.flip()
time.sleep(2)


while running:
    clock.tick(60)
    high_score = load_high_score()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            if colour == (0,128,255):
                colour = (255,100,0)
            else:
                colour = (0,128,255)


    #allow the player to move
    user_input = pygame.key.get_pressed()

    if user_input[pygame.K_UP]:
        player.move(0,-5)
    elif player.rect.y < (height -60): 
        player.move(0,5)
        
    if user_input[pygame.K_DOWN]:
        player.move(0,5)
        
    if user_input[pygame.K_LEFT]:
        player.move(-5,0)
        if player.rect.x < 0:
            player.rect.x= width -1
        
    if user_input[pygame.K_RIGHT]:
        player.move(5,0)
        if player.rect.x > width:
            player.rect.x= -59
            
##    if user_input[pygame.K_q]:
##        pygame.quit()

    if player.rect.colliderect(end_rect):
        current_score += 1
        print(current_score)
        if current_score > high_score:
            save_high_score(current_score) # update high score
            
                 
        del walls[:]
        level = random.choice(levels)
        wall_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall(x, y)
                if col == "E":
                    end_rect = pygame.Rect(x,y,30,30)
                x += 30
            y += 30
            x=0


    #draw the screen
    screen.fill((0,0,0))
    message_display("Current Score: " + str(current_score),480,480,15)
    message_display("High Score : " + str(high_score),480,500,15)

    
    for wall in walls:
        pygame.draw.rect(screen,wall_colour,wall.rect)
    pygame.draw.rect(screen,(255,0,0),end_rect)    
    pygame.draw.rect(screen,colour,player.rect)
    pygame.display.flip()

pygame.quit()














