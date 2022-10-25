import pygame

###
### Whackabox specific classes:
###

class GenerateMessage():
    def __init__(self, location=(0,0)):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.location = location
        self.name = "display_message"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            self.draw(screen)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        msgToDisplay = self.entity_state.message + self.entity_state.counter

        font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = font.render(msgToDisplay, False, (255, 255, 255))
        screen.blit(text_surface, self.location)
        return

class Move():
    def __init__(self):
        self.types = None
        self.entity_state = None
        self.verbose = False
        self.name = "move_button"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            self.draw(screen)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        import random as rand

        self.entity_state.entity_state.color = (rand.randint(10,255),rand.randint(10,255), rand.randint(10,255))
        self.entity_state.entity_state.location = (rand.randint(10,1000), rand.randint(10,600), rand.randint(100,800), rand.randint(100,800))
        self.entity_state.entity_state.actions[1].act()
        pygame.display.update()
        return

###
###  Main Game Code:
###

import enginey.engine.actor as ac
import enginey.engine.play as pl
import enginey.engine.ui as ui
import enginey.engine.utility as utl

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

###
###  HUD setup
###

new_hud = ui.make_hud([1280, 720])
sucessCnt = utl.make_success_counter("Successful Hits: ")
totalCnt = utl.make_total_counter("Total Squares: ")

sucessCnt.insert_action(GenerateMessage((10,10)))
totalCnt.insert_action(GenerateMessage((10,50)))

new_hud.insert_child(sucessCnt)
new_hud.insert_child(totalCnt)

new_hud.insert_action(ui.make_draw_hud())

game_content.append(new_hud)

###
###  Button Setup
###

starting_button_bounds = (540, 260, 200, 200)
starting_button_color = (255, 255, 255)
new_button = ui.make_basic_button("", viewer.screen, starting_button_bounds, starting_button_color)

press_action = ui.make_press_button()
press_action.children.append(Move())

new_button.insert_action(press_action)
new_button.insert_action(ui.make_draw_button())

display.insert_entity(new_button)
game_content.append(new_button)


################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()