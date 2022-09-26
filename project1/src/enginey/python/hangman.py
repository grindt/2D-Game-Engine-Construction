import pygame

from enginey.engine.play.entity.gameLoopey import gameLoopey

pygame.init()
screen = pygame.display.set_mode([1280, 720])
gameLoop = gameLoopey(screen)

while 1:
    #TODO
    #pick word
    #render everything

    gameLoop.loop()