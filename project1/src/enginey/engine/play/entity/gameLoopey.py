import pygame
import sys

class gameLoopey():
    def __init__(self, screen: pygame.surface):
        self.screen = screen

    def loop(self):
        clock = pygame.time.Clock()
        dt = 0
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quitGame()
                    #TODO
                    #pass pygame key to key handler
                    return
                if event.type == pygame.display:
                    #TODO
                    #do something with frameViewey
                    return
            dt = clock.tick(60)

    def quitGame(self):
        pygame.exit()
        sys.exit()