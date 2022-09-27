import pygame
import enginey.engine.actor as ac

class GameLoopey():
    def __init__(self, game_content):
        self.game_content = game_content
        self.word = self.game_content[len(self.game_content)-1]
        self.incorrect_guess = []
        self.correct_guess = []

    def loop(self):
        self.init_draw()
        letterHandler = ac.make_letter_handler(self.word)

        isPlaying = True
        while isPlaying:

            #do endstate checking
            if len(self.incorrect_guess) == 7:
                isPlaying = False
                self.make_sentence("You Lost Answer was: " + self.word)

            if len(self.correct_guess) == len(self.word):
                isPlaying = False
                self.make_sentence("You Won!")

            #do rendering stuff
            self.game_content[0].actions[0].act(self.game_content[0].screen)

            #do event handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quitGame()
                    guess = letterHandler.getGuess(event)
                    if letterHandler.is_correct_guess(guess):
                        self.make_letter_correct(guess)
                    else:
                        self.make_letter_incorrect(guess)
                        self.game_content[0].actions[0].make_next_body_part(self.game_content[0].screen)
        
        self.wait_for_exit()

    def wait_for_exit(self):
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quitGame()
      
    def init_draw(self):
        self.game_content[0].actions[0].init_draw(self.game_content[0].screen, len(self.game_content[0].actions[0].entities) - 7)
        return

    def quitGame(self):
        pygame.quit()
        quit()

    def make_sentence(self, sentence):
        fontSize = 40
        color = (255, 255, 255)
        location = (600, 400)
        letter_display = ac.make_basic_letter(fontSize, sentence, color, location)
        letter_display.insert_action(ac.make_draw_letter_action())
        self.game_content[0].actions[0].insert_entity(letter_display)

    def make_letter_correct(self, letter):
        fontSize = 40
        color = (255, 255, 255)
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.correct_guess.append(letter)
                location = (50 + (100 * i) + (10 * i), 620)
                letter_display = ac.make_basic_letter(fontSize, letter, color, location)
                letter_display.insert_action(ac.make_draw_letter_action())
                self.game_content[0].actions[0].insert_entity(letter_display)

    def make_letter_incorrect(self, letter):
        self.incorrect_guess.append(letter)
        fontSize = 40
        color = (255, 255, 255)
        location = (400 + (100 * len(self.incorrect_guess)) + (10 * len(self.incorrect_guess)), 100)
        letter_display = ac.make_basic_letter(fontSize, letter, color, location)
        letter_display.insert_action(ac.make_draw_letter_action())
        self.game_content[0].actions[0].insert_entity(letter_display)