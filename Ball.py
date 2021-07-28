import pygame

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (43, 43))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xdirect = 1
        self.ydirect = -1
        self.speed = 5

    
    def changexdirect(self):
        """
        Multiplies the x direction by -1
        args: none
        return: none
        """
        self.xdirect *= -1
    def changeydirect(self):
        """
        Multiplies the y direction by -1
        args: none
        return: none
        """
        self.ydirect *= -1
    
    def move(self):
        """
        Increases and decreases x and y values by speed times the direction
        args: none
        return: none
        """
        self.rect.x += self.speed * self.xdirect
        self.rect.y += self.speed * self.ydirect
    
    def goesoffbottom(self):
        """
        Lets us know if the y coordinate of the ball has a value greater than 500
        args: none
        return: True
        """
        if self.rect.y > 500:
            return True

    def goesoffside(self):
        """
        Lets us know if the x coordinate of the ball is less than 0 or greater than 470
        args: none
        return: True
        """
        if self.rect.x < 0 or self.rect.x > 470:
            return True
    
    def hitstop(self):
        """
        Lets us know if the y value of the ball is less than 0
        args: none
        return: True
        """
        if self.rect.y < 0:
            return True





    















