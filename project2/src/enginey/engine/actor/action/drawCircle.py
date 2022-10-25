import pygame
from enginey.engine.actor.entity.circle import Circle

class DrawCircleAction():
    def __init__(self):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_circle_action"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act():
            self.draw(data)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, self.entity_state.color, self.entity_state.location, self.entity_state.radius)
        return