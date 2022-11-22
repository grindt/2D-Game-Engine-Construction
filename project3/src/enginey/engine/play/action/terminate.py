import pygame

class Terminate():

    def quitGame(self):
            pygame.quit()
            quit()

    def wait_for_exit(self):
            while 1:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.quitGame()