import pygame
from enginey.engine.actor.entity.circle import Circle

class DrawHUDAction():
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_hud_action"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, args):
        if self.condition_to_act():
            self.handleChildren()
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def handleChildren(self):
        for entity in self.entity_state.children:
            if entity.active:
                for action in entity.actions:
                    if action.name == "increment":
                        action.act()
                        entity.actions.remove(action)
                    else:
                        action.act(self.entity_state.screen)
        return