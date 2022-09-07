import pygame
import random

#from random import choice
from dino_runner.components.obstacles.cactus import Cactus_Small, Cactus_Large
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
#small_large = [Cactus_Small(SMALL_CACTUS), Cactus_Large(LARGE_CACTUS),]
#qwe = choice(small_large)

class ObstacleManager:

    def __init__(self): 
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus_Small(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(Cactus_Large(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

            #if len(self.obstacles) == 0:
            #    self.obstacles.append(qwe) 
            #elif len(self.obstacles) == 1:
            #    self.obstacles.append(qwe) 

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break


    def draw(self, screen): 
        for obstacle in self.obstacles: 
            obstacle.draw(screen)