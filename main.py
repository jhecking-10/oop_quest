import pygame

from characters import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
        pygame.SCALED,
    ) # returns scaled surface object
    pygame.display.set_caption("OOP Quest")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    # load assets
    background = pygame.image.load("assets/backgrounds/simple_back.png")
    player_sprite = pygame.image.load(
        "assets/sprites/simple_wizard.png"
    ).convert_alpha() # convert pixel format for performance optimization
    player = pygame.transform.scale_by(player_sprite, 2) # double size
    
    # determine starting position on screen
    player_pos = pygame.Vector2(
        screen.get_width() / 2,
        screen.get_height() / 2,
    )
    
    print("Game loading...")
    
    while running:
        # event poll
        for event in pygame.event.get():
            # click X to close window
            if event.type == pygame.QUIT:
                running = False
                print("Game terminating...\nGoodbye")
        
        # fill screen       
        screen.fill("#ffffff") # hexadecimal white
        screen.blit(background, (0, 0))

        # render game
        screen.blit(player, player_pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip screen
        pygame.display.flip()
        
        # limit framerate
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
