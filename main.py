import pygame

# Local imports
from constants import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Refresh screen
        screen.fill(pygame.Color(0,0,0,))
        pygame.display.flip()

if __name__ == "__main__":
    main()