import pygame
from pygame.locals import *
import enginey.engine.actor as ac
import enginey.engine.play as term
import enginey.engine.utility as utl
import enginey.engine.sound as snd

class GameLoopey():
    def __init__(self, game_content):
        self.game_content = game_content
        self.events = None

    def loop(self):
        isPlaying = True
        while isPlaying:
            #get events
            self.events = pygame.event.get()

            #handle all active entities
            for entity in self.game_content:
                if entity.active:
                    for action in entity.actions:
                        self.actionHandler(action, entity)
                    for child in entity.children:
                        if child.active:
                            for action in child.actions:
                                self.actionHandler(action, child)

            #do event handling
            for event in self.events:
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    isPlaying = False

        term.make_terminate().wait_for_exit()

    def actionHandler(self, action, entity):
        if action.types[0] == "display":
            action.act(self.game_content[0].screen)

        if action.types[0] == "draw":
            action.act(self.game_content[0].screen)
            entity.actions.remove(action)

        if action.types[0] == "event":
            if action.name == "button_pressed_action":
                for event in self.events:
                    if event.type == MOUSEBUTTONDOWN:
                        if action.condition_to_act(event):
                            action.act(event)
                            self.game_content[1].children[0].insert_action(utl.make_increment())
                            self.game_content[1].children[1].insert_action(utl.make_increment())
                            self.game_content[3].insert_action(snd.make_sound_action())
                        else:
                            action.act(event)
                            self.game_content[1].children[1].insert_action(utl.make_increment())
                        break
            elif action.name == "activate_timer" \
                or action.name == "deactivate_timer" \
                or action.name == "increment" \
                or action.name == "start":
                action.act()
                entity.actions.remove(action)

            else:
                action.act()
            # maybe other unique events?

        if action.types[0] == "loop":
            action.act()