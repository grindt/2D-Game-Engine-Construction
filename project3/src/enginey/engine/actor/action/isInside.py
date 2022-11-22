import pygame

class isInside():
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.verbose = False
        self.name = "is_inside_check"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return