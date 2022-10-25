import pygame

import enginey.engine.actor as ac
import enginey.engine.play as pl

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

# make hud add 1 button in hud
# hud needs timer and counter for # of times button appears and # of succeful hits of button


################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()