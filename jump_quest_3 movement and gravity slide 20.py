import os
import random
import pygame

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


#start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#set up display
pygame.display.set_caption("Jump to escape!")
width = 620
height = 540
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
player = Player() #create a player object using the class above
colour = (0,128,255)



#start the game play!
running = True

while running:
    clock.tick(60)

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



    #draw the screen
    screen.fill((0,0,0))
    pygame.draw.rect(screen,colour,player.rect)
    pygame.display.flip()

pygame.quit()














