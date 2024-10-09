import pygame
import random

from circleshape import CircleShape
from constants import *

# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            # Spawn children
            angle = random.uniform(20, 50)
            child1Vector = self.velocity.rotate(-angle)
            child2Vector = self.velocity.rotate(angle)
            childRadius = self.radius - ASTEROID_MIN_RADIUS

            child1 = Asteroid(self.position.x, self.position.y, childRadius)
            child1.velocity = child1Vector * ASTEROID_SPEEDUP

            child2 = Asteroid(self.position.x, self.position.y, childRadius)
            child2.velocity = child2Vector * ASTEROID_SPEEDUP

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.color.Color("white"), self.position, self.radius, 2)
            
    