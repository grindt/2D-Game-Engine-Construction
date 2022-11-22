import pygame

class DrawLetterAction():
    def __init__(self):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_letter_action"
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
        font = pygame.font.SysFont('Comic Sans MS', self.entity_state.fontSize)
        text_surface = font.render(self.entity_state.letter, False, self.entity_state.color)
        screen.blit(text_surface, self.entity_state.location)
        return