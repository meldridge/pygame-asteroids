import pygame

from circleshape import CircleShape
from constants import *

# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.color.Color("white"), self.position, self.radius, 2)
            
    