import pygame

class Deactivate():
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.verbose = False
        self.name = "deactivate_timer"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            self.entity_state.active = False
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return