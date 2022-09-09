import pygame
import random

from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self): 
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE: 
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)


    def draw(self, screen): 
        for obstacle in self.obstacles: 
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []