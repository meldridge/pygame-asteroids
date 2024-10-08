import pygame

# Local imports
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

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

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initialise Player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialise an Asteroid Field
    asteroidField = AsteroidField()

    while(True):
        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Refresh screen
        screen.fill(pygame.Color("black"))

        # Render objects
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # Update: wait for next frame
        dt = clock.tick(60) / 1000

        # Process collisions
        for asteroid in asteroids:
            if player.isColliding(asteroid):
                # Oh no!
                print("Game over!")
                exit()

if __name__ == "__main__":
    main()