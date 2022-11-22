import pygame

class DrawRectangleAction():
    def __init__(self):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_rectangle_action"
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
        pygame.draw.rect(screen, self.entity_state.color, self.entity_state.bounds)
        return