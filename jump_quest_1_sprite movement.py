import os
import random
import pygame


class PlayerSprite(pygame.sprite.Sprite):
    #My sprite is going to be a rocket

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image.set_colorkey([255,255,255])

        self.rect = self.image.get_rect()

    def move(self,dx,dy):
        if dx!=0:
            self.move_single_axis(dx,0)
        if dy!=0:
            self.move_single_axis(0,dy)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        


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
screen = pygame.display.set_mode((420,340))

clock = pygame.time.Clock()
player = Player() #create a player object using the class above
player_sprite = PlayerSprite() #Creates a player sprite

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
        player_sprite.move(0,-2)
        
    if user_input[pygame.K_DOWN]:
        player_sprite.move(0,2)
        
    if user_input[pygame.K_LEFT]:
        player_sprite.move(-2,0)
        
    if user_input[pygame.K_RIGHT]:
        player_sprite.move(2,0)
    #draw the screen
    screen.fill((0,0,0))
    pygame.draw.rect(screen,colour,player.rect)

    all_sprites_list = pygame.sprite.Group()
    
#     player_sprite.rect.x = 100
#     player_sprite.rect.y = 100
    all_sprites_list.add(player_sprite)

    all_sprites_list.draw(screen)

    
    pygame.display.flip()

pygame.quit()



















