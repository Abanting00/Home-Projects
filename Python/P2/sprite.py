#Testing Sprites by creating a block collision game
#The goal of the game is to collect all the falling blocks and by moving using 
#the keyboard

import pygame
import random
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)         #Allows the parent to initialize

        self.image = pygame.Surface([width,height]) #Create an image of block
        self.image.fill(color)                      #can be replaced with loaded image

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > 400:
            self.rect.y = random.randrange(-100,-10)
            self.rect.x = random.randrange(0, 700)

 
def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [700, 400]
    screen = pygame.display.set_mode(size)

    block_list = pygame.sprite.Group()
 
    all_sprites_list = pygame.sprite.Group()

    pygame.display.set_caption("My Game")
 

    for i in range(50):
        block = Block(BLACK,20,15)

        block.rect.x = random.randrange(700)
        block.rect.y = random.randrange(400)

        block_list.add(block)
        all_sprites_list.add(block)

    player = Block(RED,20,15)
    all_sprites_list.add(player)

    player.rect.x = 350
    player.rect.y = 220

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    score = 0
    x_speed = 0
    y_speed = 0
    
    pygame.mouse.set_visible(False)
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                if event.key == pygame.K_RIGHT:
                    x_speed = 5
                if event.key == pygame.K_UP:
                    y_speed = -5
                if event.key == pygame.K_DOWN:
                    y_speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        player.rect.x += x_speed
        player.rect.y += y_speed

        block_list.update()


        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        #Check the list of collisions from the line above
        for block in block_hit_list:
            score += 1
            print(score)

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(WHITE)
 
        all_sprites_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()