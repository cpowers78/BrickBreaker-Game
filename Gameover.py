import pygame

class Gameover(pygame.sprite.Sprite):
    #initializes the images
    def __init__(self, x, y, fn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fn)
        self.image = pygame.transform.scale(self.image, (500, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def changebrainsize(self):
        """
        Changed the size of the brain image on the start screen
        args: none
        return: none
        """
        self.image = pygame.transform.scale(self.image, (500, 500))
    
    def changethumbsize(self):
        """
        Change the thumb size on the screen when the user has won the game
        args: none
        return: none
        """
        self.image = pygame.transform.scale(self.image, (50, 50))

    def changestartsize(self):
        """
        Changes the size of the start button
        args: none
        return: none
        """
        self.image = pygame.transform.scale(self.image, (300,200))

