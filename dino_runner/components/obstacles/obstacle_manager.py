import pygame
import random

from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD

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
                if game.player.type != SHIELD_TYPE and game.player.type != HAMMER_TYPE: 
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.type == HAMMER_TYPE:
                    
                    self.hammer_obstacle(game)
                else:
                    self.obstacles.remove(obstacle)
            
            elif game.player.dino_rect.colliderect(obstacle.rect):
                self.tries -= 1
                game.lives_manager.reduce_heart()
                game.playing = True
                if self.tries != 0:
                    self.obstacles.remove()
                else:
                    pygame.time.delay(500)
                    game.death_count += 1
                    break

    def hammer_obstacle(self, game):
        for obstacle in self.obstacles:
            if game.player.dino_rect.colliderect(obstacle.rect):
                obstacle.rect.x += game.game_speed * 2
                obstacle.rect.y -= game.game_speed * 2
            if obstacle.rect.x > 1300:
                self.obstacles.pop()

    def draw(self, screen): 
        for obstacle in self.obstacles: 
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        self.tries = 5