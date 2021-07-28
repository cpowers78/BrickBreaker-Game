import pygame

class Slider(pygame.sprite.Sprite):
    def __init__(self, y, fn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fn)
        self.image = pygame.transform.scale(self.image, (85, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 480
        self.speed = 25
        self.direction = 'l'
    
    def move_left(self):
        """
        Moves the slider to the left by decreasing its x value by the speed
        args: none
        return: none
        """
        self.rect.x -= self.speed
    def move_right(self):
        """
        Moves the slider to the right by increasing its x value by the speed
        args: none
        return: none
        """
        self.rect.x += self.speed
    
  
