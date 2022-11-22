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
        if len(self.entities) > 0:
            return True
        return False

    def act(self, data):
        if self.condition_to_act():
            self.make_entity_act(data)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        pygame.display.flip()
        return

    def make_entity_act(self, screen):
        screen.fill((0,0,0))
        for entity in self.entities:
            if entity.active:
                for action in entity.actions:
                    if(action.types[0] == "draw"):
                        action.act(screen)
        return