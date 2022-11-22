from pygame.locals import *
import enginey.engine.utility as utl

class ButtonPressed:
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "button_pressed_action"
        self.children = []

    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return self.entity_state.is_inside(event.pos)

    def act(self, *args):
        for c in self.children:
            c.act(self.entity_state.screen)
        self.entity_state.children[0].insert_action(utl.make_start())
        self.entity_state.children[0].active = True
        return

    def insert_child(self, c):
        c.entity_state = self
        self.children.append(c)
        return