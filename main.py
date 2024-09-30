import pygame

# Local imports
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialise clock
    clock = pygame.time.Clock()
    dt = 0

    # Initialise screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialise Player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Refresh screen
        screen.fill(pygame.Color("black"))

        # Render player
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

        # Wait for next frame
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()