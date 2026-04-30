import pygame

class Score():

    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        pass

    def increase(self, points):
        self.score += points
        self.image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.rect = self.image.get_rect()