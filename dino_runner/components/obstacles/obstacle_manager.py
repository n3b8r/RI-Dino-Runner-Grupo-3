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
            self.obstacle_type_list = [Bird(), SmallCactus(SMALL_CACTUS), LargeCactus(LARGE_CACTUS),] 
            self.obstacles.append(random.choice(self.obstacle_type_list))

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