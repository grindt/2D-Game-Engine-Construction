from enginey.engine.actor.entity.letter import Letter
import pygame

class FrameVieweyAction():
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "frame_viewey_action"
        self.entities = []
        return

    def insert_entity(self, e):
        self.entities.append(e)
        return

    def condition_to_act(self):
        if len(self.entities) > 0 and (type(self.entities[len(self.entities)-1]) == type(Letter(0, "s"))):
            return True
        return False

    def act(self, data):
        while self.condition_to_act():
            self.make_entity_act(data)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        pygame.display.flip()
        return

    def make_entity_act(self, screen):
        self.entities.pop().actions[0].act(screen)
        return

    def init_draw(self, screen, num):
        for i in range(num):
            self.entities.pop(0).actions[0].act(screen)
        pygame.display.flip()
        return

    def make_next_body_part(self, screen):
        self.entities.pop(0).actions[0].act(screen)
        pygame.display.flip()
        return