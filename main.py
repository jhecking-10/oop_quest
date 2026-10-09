import pygame

from characters import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def inititalize():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    dt = 0
    return clock, running, dt

def create_screen():
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
        pygame.SCALED,
        vsync=1,
    )
    pygame.display.set_caption("OOP Quest")
    return screen

def fill_screen(screen, background):
    screen.fill("#ffffff")
    screen.blit(background, (0, 0))

def set_controls(pos, spd, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos.y -= spd * dt
    if keys[pygame.K_s]:
        pos.y += spd * dt
    if keys[pygame.K_a]:
        pos.x -= spd * dt
    if keys[pygame.K_d]:
        pos.x += spd * dt

def main():
    clock, running, dt = inititalize()
    screen = create_screen()
    
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
        fill_screen(screen, background)

        # render game
        set_controls(player_pos, 150, dt)
        screen.blit(player, player_pos)

        # flip screen
        pygame.display.flip()
        
        # limit framerate
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
