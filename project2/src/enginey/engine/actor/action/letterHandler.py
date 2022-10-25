import pygame
import enginey.engine.actor as ac

class LetterHandler():
    def __init__(self, word):
        self.types = ["event"]
        self.name = "letter_handler"
        self.word = word
        return
    
    def is_correct_guess(self, guess):
        for letter in self.word:
            if letter == guess:
                return True
        return False

    def getLetter(self, e):
        if e.key == pygame.K_a:
            return 'a'
        if e.key == pygame.K_b:
            return 'b'
        if e.key == pygame.K_c:
            return 'c'
        if e.key == pygame.K_d:
            return 'd'
        if e.key == pygame.K_e:
            return 'e'
        if e.key == pygame.K_f:
            return 'f'
        if e.key == pygame.K_g:
            return 'g'
        if e.key == pygame.K_h:
            return 'h'
        if e.key == pygame.K_i:
            return 'i'
        if e.key == pygame.K_j:
            return 'j'
        if e.key == pygame.K_k:
            return 'k'
        if e.key == pygame.K_l:
            return 'l'
        if e.key == pygame.K_m:
            return 'm'
        if e.key == pygame.K_n:
            return 'n'
        if e.key == pygame.K_o:
            return 'o'
        if e.key == pygame.K_p:
            return 'p'
        if e.key == pygame.K_q:
            return 'q'
        if e.key == pygame.K_r:
            return 'r'
        if e.key == pygame.K_s:
            return 's'
        if e.key == pygame.K_t:
            return 't'
        if e.key == pygame.K_u:
            return 'u'
        if e.key == pygame.K_v:
            return 'v'
        if e.key == pygame.K_w:
            return 'w'
        if e.key == pygame.K_x:
            return 'x'
        if e.key == pygame.K_y:
            return 'y'
        if e.key == pygame.K_z:
            return 'z'
