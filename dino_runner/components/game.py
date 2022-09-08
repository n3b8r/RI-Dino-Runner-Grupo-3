import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, BIRD, CLOUD, FONT_STYLE, ICON, LIVE_ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

        self.running = False
        self.score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.score = 0
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(F"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        print(self.death_count)
        self.screen.fill((181, 178, 178))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
            
            self.screen.blit(LIVE_ICON, (half_screen_width -20, half_screen_height - 140))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))  
        else:
            font = pygame.font.Font(FONT_STYLE, 50)
            text = font.render("GAME OVER", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (610, 80)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 50)
            text = font.render("PRESS ANY KEY TO REBOOT", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (610, 520)
            self.screen.blit(text, text_rect)
            
            font = pygame.font.Font(FONT_STYLE, 40)
            text = font.render(F"Deaths: {self.death_count}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (600, 300)
            self.screen.blit(text, text_rect)

            text = font.render(F"Total score: {self.score}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (600, 400)
            self.screen.blit(text, text_rect)

            self.game_speed = 15
            self.screen.blit(ICON, (half_screen_width -20, half_screen_height - 140))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))   

             
        
        pygame.display.update()
        self.handle_events_on_menu()