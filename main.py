import pygame

from characters import *


def main():
    # basic pygame setup according to docs
    pygame.init()
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    running = True
    dt = 0
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
        
        # fills screen to wipe away last frame        
        screen.fill("purple")

        # render game between filling the
        # screen and flipping the display
        pygame.draw.circle(screen, "black", player_pos, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # puts game on screen
        pygame.display.flip()
        
        # limit framerate
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
