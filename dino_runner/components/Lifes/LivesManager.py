from dino_runner.components.Lifes.lifes import Heart


class LivesManager:
    def __init__(self):
        self.lifes_count = 5

    def reduce_heart(self):
        self.lifes_count -= 1

    def draw(self, screen):
        x_position = 20
        y_position = 10

        for i in range(self.lifes_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30

    def reset_hearts(self):
        self.lifes_count = 5