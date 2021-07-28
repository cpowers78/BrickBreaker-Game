import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (63, 38))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
