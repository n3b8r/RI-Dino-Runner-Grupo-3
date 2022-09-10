import pygame
from dino_runner.components.Lifes.LivesManager import LivesManager
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, CLOUD, DEFAULT_TYPE, FONT_STYLE, ICON, LIVE_ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


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
        self.power_up_manager = PowerUpManager()
        self.lives_manager = LivesManager()

        self.running = False
        self.score = 0
        self.max_score = 0
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
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 15
        self.score = 0
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
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3
        if self.max_score < self.score:         # para obtener el maximo puntaje
            self.max_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        if self.score <= 1000:
            self.screen.fill((250, 250, 250)) 
        else:
            self.screen.fill((205, 205, 205)) # cambio de color de la pantalla
        self.draw_background()
        self.draw_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
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
        self.place_text(22, 1000, 50, F"Score: {self.score}", (0, 0, 0))
        self.place_text(22, 970, 70, F"Hight Score: {self.max_score}", (0, 0, 0))
 
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.", True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (550, 50)
                self.screen.blit(text, text_rect)
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def place_text(self, font_sizes, pos_x, pos_y, text_message, color):
        font = pygame.font.Font(FONT_STYLE, font_sizes)
        text = font.render(text_message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        print(self.death_count)
        self.screen.fill((205, 205, 205))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.place_text(30, half_screen_width, half_screen_height, "Press any key to start", (0, 0, 20))
            self.screen.blit(LIVE_ICON, (half_screen_width -20, half_screen_height - 140))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))  
        else:
            self.place_text(50, 610, 80, "GAME OVER", (255, 0, 0))
            self.place_text(50, 610, 520, "PRESS ANY KEY TO REBOOT", (0, 0, 180))
            self.place_text(40, 600, 300, f"Deaths: {self.death_count}", (255, 100, 32))
            self.place_text(40, 600, 400, f"Total score: {self.score}", (255, 100, 32))
            self.screen.blit(ICON, (half_screen_width -20, half_screen_height - 140))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))   
      
        pygame.display.update()
        self.handle_events_on_menu()