from random import choice
from random import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus_Small, Cactus_Large
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

small_large_cactus = [
    Cactus_Small(SMALL_CACTUS),
    Cactus_Large(LARGE_CACTUS),
]
value = choice(small_large_cactus)

class ObstacleManager:

    def __init__(self): 
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0: 
            self.obstacles.append.list(value)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break


    def draw(self, screen): 
        for obstacle in self.obstacles: 
            obstacle.draw(screen)