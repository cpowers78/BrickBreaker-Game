import sys
import pygame
import random
import time
from src import Ball
from src import Block
from src import Slider
from src import Gameover

class Controller:
    def __init__(self):
#This stuff is necessary to make the screen and is used later on when we redraw it
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.slider = Slider.Slider((250,480), "assets/slider.png")

        self.blocks = pygame.sprite.Group()
        for i in range(7):
            for j in range (0,4):
                x = (8+ i * 70)
                y = (10 + j * 50)
                self.blocks.add(Block.Block(x, y, 'assets/block.png' ))

        self.ball = Ball.Ball(250,250, "assets/virus.png")
        self.all_sprites = pygame.sprite.Group((self.slider,)+tuple(self.blocks) + (self.ball,))

        self.count = 0
        self.STATE = "screen"

        self.picture = Gameover.Gameover(0,150, "assets/GAMEOVER.png")
        self.wonpicture = Gameover.Gameover(0,150, "assets/YOUWIN.png")


    def mainloop(self):
        """
        Is the mainloop which determines if the game plays, exits, wins, or loses
        args: None
        return: None
        """
        while True:
            if self.STATE == "game":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()
            elif self.STATE == "screen":
                self.startloop()
            elif self.STATE == "lost":
                self.lostgame()
            elif self.STATE == "won":
                self.wongame()


    def startloop(self):
        """
        Creates the start screen for the game, press the start button to start the game
        args: None
        return: None
        """
        self.cover = Gameover.Gameover(0,1, "assets/COVERPAGE.png")
        self.cover.changebrainsize()
        self.startbutton = Gameover.Gameover(115, 350, "assets/startbutton.png")
        self.startbutton.changestartsize()
        self.background.fill((255,255,255))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.cover.image, (self.cover.rect.x, self.cover.rect.y))
        self.screen.blit(self.startbutton.image, (self.startbutton.rect.x, self.startbutton.rect.y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.startbutton.rect.collidepoint(event.pos)):
                    self.STATE = "game"

    def exitloop(self):
        """
        Exits the game/program
        args: None
        return: None
        """
        pygame.quit()
        exit()

    def gameloop(self):
        """
        Contains eventloop for the game. Sets framerate to 30. Sets controls. Sets what happens when the ball collides with objects. Includes update method for objects and updates the screen.
        args: None
        return: None
        """
        pygame.key.set_repeat(1,40)

        clock = pygame.time.Clock()

        while self.STATE == "game":
            self.ball.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.slider.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.slider.move_right()
                    if event.key == pygame.K_a:
                        self.slider.move_left()
                    if event.key == pygame.K_d:
                        self.slider.move_right()

            sliderhit = pygame.sprite.collide_rect(self.ball, self.slider)
            if (sliderhit):
                self.ball.changeydirect()

            brickhit = pygame.sprite.spritecollide(self.ball, self.blocks, True)
            for b in (brickhit):
                if (brickhit):
                    self.ball.changeydirect()
                    b.kill()

            if self.ball.goesoffside():
                self.ball.changexdirect()

            if self.ball.goesoffbottom():
                self.count += 1
                self.ball.rect.x = 250
                self.ball.rect.y = 250

            if self.ball.hitstop():
                self.ball.changeydirect()

            if self.count == 3:
                self.STATE = "lost"

            if (len(self.blocks) == 0):
                self.STATE = "won"

#This stuff redraws the background and slider it is needed otherwise the program wont run
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.slider.image, (self.slider.rect.x, self.slider.rect.y))
            self.background.fill((0,0,75))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(30)

    def lostgame(self):
        """
        Loads up the "GAME OVER" screen if you lose the game.
        args: None
        return: None
        """
        self.picture = Gameover.Gameover(0,150, "assets/GAMEOVER.png")
        self.background.fill((0,0,0))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.picture.image, (self.picture.rect.x, self.picture.rect.y))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def wongame(self):
        """
        Loads up the win screen if you win the game. If you click the thumbs up picture you go back to the start screen. If you press thumbs down it ends the program.
        args: None
        return: None
        """
        self.wonpicture = Gameover.Gameover(0,150, "assets/YOUWIN.png")
        self.thumbsup = Gameover.Gameover(150, 375, "assets/thumbsup.png")
        self.thumbsup.changethumbsize()
        self.thumbsdown = Gameover.Gameover(250, 375, "assets/thumbsdown.png")
        self.thumbsdown.changethumbsize()
        self.background.fill((255,255,255))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.wonpicture.image, (self.wonpicture.rect.x, self.wonpicture.rect.y))
        self.screen.blit(self.thumbsup.image, (self.thumbsup.rect.x, self.thumbsup.rect.y))
        self.screen.blit(self.thumbsdown.image, (self.thumbsdown.rect.x, self.thumbsdown.rect.y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(self.thumbsdown.rect.collidepoint(event.pos)):
                    sys.exit()
                if(self.thumbsup.rect.collidepoint(event.pos)):
                    self.STATE = "game"
                    self.__init__()
                    self.startloop()
