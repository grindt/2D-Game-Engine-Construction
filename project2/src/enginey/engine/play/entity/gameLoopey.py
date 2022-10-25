import pygame
import enginey.engine.actor as ac
import enginey.engine.play as term

class GameLoopey():
    def __init__(self, game_content):
        self.game_content = game_content
        self.terminate = term.make_terminate()
        self.word = self.game_content[len(self.game_content)-1]
        self.incorrect_guess = []
        self.correct_guess = []

    def loop(self):
        self.init_draw()
        letterHandler = ac.make_letter_handler(self.word)

        isPlaying = True
        while isPlaying:

            #do rendering stuff
            self.game_content[0].actions[0].act(self.game_content[0].screen)

            #do event handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.terminate.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.terminate.quitGame()
                    guess = letterHandler.getGuess(event)
                    if letterHandler.is_correct_guess(guess):
                        self.make_letter_correct(guess)
                    else:
                        self.make_letter_incorrect(guess)
                        self.game_content[0].actions[0].make_next_body_part(self.game_content[0].screen)
        
        self.terminate.wait_for_exit()
      
    def init_draw(self):
        self.game_content[0].actions[0].init_draw(self.game_content[0].screen, len(self.game_content[0].actions[0].entities) - 7)
        return

    def make_sentence(self, sentence):
        fontSize = 40
        color = (255, 255, 255)
        location = (600, 400)
        letter_display = ac.make_basic_letter(fontSize, sentence, color, location)
        letter_display.insert_action(ac.make_draw_letter_action())
        self.game_content[0].actions[0].insert_entity(letter_display)